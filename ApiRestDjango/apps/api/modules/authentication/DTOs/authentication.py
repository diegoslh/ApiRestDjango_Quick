from typing import Self


class AuthenticationDTO:
    def __init__(self: Self, user: dict):
        self.id = user.id
        self.email = user.email
        self.typology = user.typology
        self.first_name = user.first_name
        self.last_name = user.last_name

    def data(self):
        return {
            "id": self.id,
            "typology": self.typology,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
