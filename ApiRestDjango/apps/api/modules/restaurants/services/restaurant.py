from typing import Self
from rest_framework.serializers import ValidationError
from modules.restaurants.utilities.enum import RestaurantStatusEnum


class RestaurantValidateService:

    def __init__(self: Self, *, data: dict):
        self.data = data

    def _validate_data(self: Self):

        if self.data.get("rating"):
            self._validate_rating(self.data["rating"])

        if self.data.get("status"):
            self._validate_status(self.data["status"])

    def _validate_rating(self: Self, rating: float):
        if not (0 <= rating <= 5):
            raise ValidationError("El rating debe estar entre 0 y 5")

    def _validate_status(self: Self, status: str):
        if status not in [
            RestaurantStatusEnum.OPEN.value,
            RestaurantStatusEnum.CLOSED.value,
        ]:
            raise ValidationError("El estado debe ser Abierto o Cerrado.")
