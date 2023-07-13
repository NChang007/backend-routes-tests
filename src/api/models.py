from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# comments = db.Table(
#     'comments',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('discussion_id', db.Integer, db.ForeignKey('discussion.id'), primary_key=True)
# )

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)

    discussions = db.relationship("Discussion", back_populates="created_by", foreign_keys='Discussion.user_id')
    comments = db.relationship("Comment", back_populates="created_by", foreign_keys='Comment.user_id')

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Discussion(db.Model):
    __tablename__= 'discussions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=False, nullable=False)
    discussion = db.Column(db.String(500), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_by = db.relationship("User", back_populates="discussions", foreign_keys=[user_id])
    disc_comments = db.relationship('Comment', backref='discussion', lazy=True)


    def __repr__(self):
        return f'<Discussion {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            'discussion': self.discussion,
            'createdBy': self.created_by.serialize(),
            'comments' : [comment.serialize() for comment in self.disc_comments]
        }

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    discussion_id = db.Column(db.Integer, db.ForeignKey("discussions.id"), nullable=False)
    comment = db.Column(db.String(500), unique=False, nullable=False)
    
    created_by = db.relationship("User", back_populates="comments", foreign_keys=[user_id])

    def __repr__(self):
        return f'<Comment {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            # "discussion_id": self.discussion_id,
            'created_by': self.created_by.serialize(),
            'comment' : self.comment,
        }