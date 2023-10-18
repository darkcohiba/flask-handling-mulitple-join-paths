#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import User, FriendShip
from config import db
fake = Faker()

def create_users():
    users = []
    for _ in range(15):
        u = User(
            username = fake.name(),
            email = fake.email(),
            password_hash = "123abc", 
        )
        users.append(u)
    return users




if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # delete users
        print("delete data")
        db.session.query(User).delete()
        db.session.query(FriendShip).delete()
        db.session.commit()

        print("creating users")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        

        
        