from typing import Self
from rest_framework.serializers import ValidationError
from modules.users.utilities.enum import UserTypologyEnum
from modules.users.models.user import User


class UserValidateService:

    def __init__(self: Self, *, data: dict):
        self.data = data

    def _validate_data(self: Self):

        self._validate_password()
        self._validate_email()

        if self.data.get("typology"):
            self._validate_typology(self.data["typology"])

    def _validate_typology(self: Self, typology: str):
        if typology not in [
            UserTypologyEnum.DEALER.value,
            UserTypologyEnum.CUSTOMER.value,
        ]:
            raise ValidationError("Only Dealer or Customer typology is allowed.")

    def _validate_email(self: Self):
        email = self.data.get("email")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")

    def _validate_password(self: Self):
        password = self.data.get("password")

        if not password:
            raise ValidationError("Password is required.")

        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
