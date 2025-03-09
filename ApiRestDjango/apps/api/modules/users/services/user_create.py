from typing import Self
from django.db import transaction
from rest_framework.serializers import ValidationError
from modules.users.models import User, UserCredentials
from modules.users.services.user import UserValidateService
from modules.shared.utilities.encryption import EncryptionService


class UserCreateService(UserValidateService):

    def __init__(self: Self, *, data: dict):
        super().__init__(data=data)

    def create(self: Self) -> User:
        try:
            with transaction.atomic():
                self._validate_data()
                password = self.data.pop("password")
                encrypted_password = EncryptionService.encrypt_password(password)
                user: User = User.objects.create(**self.data)
                UserCredentials.objects.create(
                    user_id=user, password=encrypted_password
                )
                return user

        except Exception as e:
            raise ValidationError(str(e))
