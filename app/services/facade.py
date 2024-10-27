from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place  
from flask_restx import marshal
from flask import Flask, jsonify

class HBnBFacade:
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HBnBFacade, cls).__new__(cls)
            cls._instance.user_repo = InMemoryRepository()
            cls._instance.place_repo = InMemoryRepository()
            cls._instance.review_repo = InMemoryRepository()
            cls._instance.amenity_repo = InMemoryRepository()
        return cls._instance

    """
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    


    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return (user)

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
    
    def get_user(self, id): 
        return self.user_repo.get(id)
    

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
               
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("user not foud")

        for key, value in user_data.items():
            if hasattr(user, key):  
                setattr(user, key, value)


        self.user_repo.update(user.id, user_data)
        return user
    


    @classmethod
    def create_review():
        pass

    def create_place(self, place_data):
        """removing owner_id from place_data"""
        owner_id = place_data.pop('owner_id')

        """get user object """
        owner = self.get_user(owner_id)

        """Add User object to the place_data"""
        place_data['owner'] = owner

        """creating the place """
        place = Place(**place_data)

        """storing the place in repo"""
        self.place_repo.add(place)

        """adding back the owner_id for client response"""

        place_data['owner_id'] = owner_id

        """returning place object and owner_id for client response"""
        return place_data

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        pass

facade =  HBnBFacade()