from django.db import models
from modules.shared.models.basicModel import basicModel


class RestaurantCategory(basicModel):
    class Meta(basicModel.Meta):
        db_table = "restaurant_category"

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45)
