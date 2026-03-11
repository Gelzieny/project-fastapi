class UserRegister:
    def __init__(self, user_service):
        self.user_service = user_service

    def register(self, user_data):
        # Validate user data (e.g., check for required fields, email format, etc.)
        if not self.validate_user_data(user_data):
            return {"error": "Invalid user data"}, 400

        # Check if the user already exists
        if self.user_service.get_user_by_email(user_data['email']):
            return {"error": "User already exists"}, 400

        # Create the user
        new_user = self.user_service.create_user(user_data)
        return {"message": "User registered successfully", "user": new_user}, 201

    def validate_user_data(self, user_data):
        # Implement validation logic (e.g., check for required fields, email format, etc.)
        required_fields = ['email', 'password', 'name']
        for field in required_fields:
            if field not in user_data:
                return False
        # Additional validation can be added here (e.g., email format)
        return True