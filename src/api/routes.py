"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Discussion, Comment
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

api = Blueprint('api', __name__)


# login Route-----------------------------------------------------------------------------
@api.route("/login", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if not email:
        return jsonify({"msg": "Email is required"}), 400
    if not password:
        return jsonify({"msg": "Password is required"}), 400
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "Email/Password are incorrect"}), 401
    if not check_password_hash(user.password, password):
        return jsonify({"msg": "Username/Password are incorrect"}), 401
    # create token
    expiration = datetime.timedelta(days=3)
    token = create_access_token(identity= user.id, expires_delta= expiration)
    return jsonify(token=token)

# create user -----------------------------------------------------------------------------------------------------------
@api.route('/createUser', methods=['POST'])
def createUser():
    request_body = request.get_json()
    if not request_body["name"]:
      return jsonify({"msg": "Name is required"}), 400
    if not request_body["email"]:
      return jsonify({"msg": "Email is required"}), 400
    if not request_body["password"]:
      return jsonify({"msg": "Password is required"}), 400
    user = User.query.filter_by(email=request_body["email"]).first()
    if user:
      return jsonify({"msg": "User already exists"}), 400
    user = User(
          name = request_body["name"],
          email = request_body["email"],
        #   password = generate_password_hash(request_body["password"]),
      )
    db.session.add(user)
    db.session.commit()
    return jsonify({"created": "Thanks. Your registration was successfully", "status": "true"}), 200


# GET ALL USERS
@api.route('/users', methods=['GET'])
def getAllUsers():
    users = User.query.all()
    users_dic = [user.serialize() for user in users]
    return jsonify(users_dic), 200

# GET ONE DISCUSSION
@api.route('/oneUsers', methods=['GET'])
def getOneUser():
    user_id = 1
    user = User.query.get(user_id)
    return jsonify(user.serialize())

# UPDATE USER
@api.route("/updateUser", methods=["PUT"])
# @jwt_required()
def update_user():
    # Retrieve the data from the request
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # Get the current user from the JWT identity
    # user_id = get_jwt_identity()
    user_id = 1
    user = User.query.get(user_id)

    # Update the user's profile
    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    if password is not None:
        user.password = password #this need to ne hashed

    db.session.commit()

    # Return a success response
    return jsonify({"message": "Profile updated successfully"}), 200

# GET ALL DISCUSSIONS
@api.route('/discussions', methods=['GET'])
def getAllDiscussions():
    discussions = Discussion.query.all()
    discussions_dic = [discussion.serialize() for discussion in discussions]
    return jsonify(discussions_dic), 200

# GET ONE DISCUSSION
@api.route('/discussions/<int:id>', methods=['GET'])
def getOneDiscussions(id):
    discussion = Discussion.query.get(id)
    return jsonify(discussion.serialize())

# CREATE DISCUSSION
@api.route('/discussions', methods=['POST'])
# @jwt_required()
def createDiscussion():
    # user_id = get_jwt_identity()
    user_id = 1
    body = request.get_json()
    new_disc = Discussion (
        user_id=user_id,
        title=body["title"],
        discussion=body["discussion"]
    )
    db.session.add(new_disc)
    db.session.commit()
    return jsonify(new_disc.serialize()), 200

# CREATE COMMENT
@api.route('/comment', methods=['POST'])
# @jwt_required()
def createComment():
    # user_id = get_jwt_identity()
    user_id = 1
    data = request.json
    body = request.get_json()
    new_comment = Comment (
        user_id=user_id,
        discussion_id=body["discussion_id"],
        comment=body["comment"],
        parent_id=data.get("parent_id") or None
    )
    db.session.add(new_comment)
    db.session.commit()
    discussion = Discussion.query.get(body["discussion_id"])
    return jsonify(discussion.serialize()), 200



@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200