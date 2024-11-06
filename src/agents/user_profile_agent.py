class UserProfileAgent:
    def __init__(self):
        # Initialize any necessary configurations or connections
        pass

    def get_user_profile(self):
        # Static test data representing a sample user profile
        user_profile = {
            "user_id": "12345",
            "name": "John Doe",
            "car_model": "Toyota Camry 2021",
            "service_history": ["Oil change", "Brake pad replacement", "Battery check"],
            "preferences": {
                "language": "English",
                "units": "metric"
            }
        }
        return user_profile
