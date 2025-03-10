from django.db import models
from modules.shared.models.basicModel import basicModel
from modules.restaurants.models.restaurant import Restaurant


class User(basicModel):
    class Meta:
        db_table = "user"

    id = models.AutoField(primary_key=True)
    typology = models.CharField(max_length=10)
    restaurant_id = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_id"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    default_address = models.TextField()


class UserCredentials(basicModel):
    class Meta:
        db_table = "user_credential"

    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_id"
    )
    password = models.BinaryField()
