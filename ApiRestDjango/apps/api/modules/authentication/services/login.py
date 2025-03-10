from typing import Self
from rest_framework.serializers import ValidationError
from modules.users.models import User, UserCredentials
from modules.shared.utilities.encryption import EncryptionService
import datetime
import jwt


class LoginService:
    def __init__(self: Self, *, data: dict):
        self.data = data

    def validate_credentials(self: Self) -> User:
        try:
            user: User = User.objects.get(email=self.data.get("email"))
            if not user.active:
                raise ValidationError("User disabled")

            encrypted_password = UserCredentials.objects.get(user_id=user).password
            if isinstance(encrypted_password, memoryview):
                encrypted_password = bytes(encrypted_password)

            password_form = self.data.get("password")
            comparation_passwords = EncryptionService.verify_password(
                password_form, encrypted_password
            )

            if comparation_passwords:
                return user
            raise ValidationError("Invalid password")

        except User.DoesNotExist:
            raise ValidationError("Invalid user")

    @staticmethod
    def create_token(user_data: dict) -> str:
        payload: dict = {
            "user_id": user_data["id"],
            "username": user_data["email"],
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(hours=5),
        }

        token: str = jwt.encode(payload, "OUH85S", algorithm="HS256")

        return token
