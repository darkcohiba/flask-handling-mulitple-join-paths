from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable=False)

    requestor = db.relationship('FriendShip', back_populates="requestor")
    requested = db.relationship('FriendShip', back_populates="requested")



    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
class FriendShip(db.Model, SerializerMixin):
    __tablename__ = 'friendship_table'
    id = db.Column(db.Integer, primary_key=True)
    requestor_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))
    requested_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))


    requestor = db.relationship('User', back_populates="requestor")
    requested = db.relationship('User', back_populates="requested")
    # requestor = db.relationship('User', back_populates="requestor", foreign_keys=[requestor_id])
    # requested = db.relationship('User', back_populates="requested", foreign_keys=[requested_id])