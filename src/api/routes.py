"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Discussion, Comment
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# GET ALL USERS
@api.route('/users', methods=['GET'])
def getAllUsers():
    users = User.query.all()
    users_dic = [user.serialize() for user in users]
    return jsonify(users_dic), 200

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
        user.password = password

    db.session.commit()

    # Return a success response
    return jsonify({"message": "Profile updated successfully"}), 200

# GET ALL DISCUSSIONS
@api.route('/discussions', methods=['GET'])
def getAllDiscussions():
    discussions = Discussion.query.all()
    discussions_dic = [discussion.serialize() for discussion in discussions]
    return jsonify(discussions_dic), 200

# CREATE DISCUSSION
@api.route('/discussions', methods=['POST'])
def createDiscussion():
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
def createComment():
    user_id = 1
    discussion_id = 1
    body = request.get_json()
    new_comment = Comment (
        user_id=user_id,
        discussion_id=body["discussion_id"],
        comment=body["comment"],
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment.serialize()), 200



@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200