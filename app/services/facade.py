from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place      

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
    


    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
    
    def get_user(self, user_id): 
        return self.user_repo.get(user_id)
    

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
               
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("user not foud")
            return 404

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']

        self.user_repo.update(user.id, {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            })
        return user
    


    @classmethod
    def create_review():
        pass

    def create_place(self, place_data):
        """poping owner_id from api payload"""
        owner_id = place_data.get('owner_id', None)
        """geting the owner object from the repo"""
        owner = self.get_user(owner_id)
        if owner is None:
            raise ValueError(f"Owner ID : {owner_id} not found")
                
        """removing the reviews and amenities from the payload"""
        reviews = place_data.pop('reviews', [])
        amenities = place_data.pop('amenities', [])

        """creating the place and adding the owner object"""
        place = Place(**place_data)

        """adding back previously removed field"""
        place.reviews = reviews
        place.amenities = amenities

        """storing the place in repo"""
        self.place_repo.add(place)
        return place

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