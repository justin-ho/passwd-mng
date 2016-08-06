class UserAccountNotFoundError(Exception):
    message = "User Account Not Found"

    def __init__(self, message):
        self.message = message
