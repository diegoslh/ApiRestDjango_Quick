from typing import Self
from django.db import transaction
from rest_framework.serializers import ValidationError
from modules.users.models import User, UserCredentials
from modules.users.services.user import UserValidateService
from modules.shared.utilities.encryption import EncryptionService


class UserUpdateService(UserValidateService):

    def __init__(self: Self, *, data: dict):
        super().__init__(data=data)

    @transaction.atomic
    def update(self: Self) -> User:
        try:
            self._validate_data()
            id_user = self.data.pop("id")
            password = self.data.pop("password")

            user: User = User.objects.filter(id=id_user).first()
            if not user:
                raise ValidationError("User not found")

            for key, value in self.data.items():
                setattr(user, key, value)
            user.save()

            if password:
                encrypted_password = EncryptionService.encrypt_password(password)
                UserCredentials.objects.filter(user_id=user).update(
                    password=encrypted_password
                )
            return user

        except ValidationError as e:
            raise ValidationError(e.detail)

    def inactivate(self: Self) -> None:
        id_user = self.data.get("id")
        if not id_user:
            raise ValidationError("ID is required")

        User.objects.filter(id=id_user).update(active=False)
        UserCredentials.objects.filter(user_id=id_user).update(active=False)
