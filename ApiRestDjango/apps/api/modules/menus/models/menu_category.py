from django.db import models
from modules.shared.models.basicModel import basicModel


class MenuCategory(basicModel):
    class Meta(basicModel.Meta):
        db_table = "menu_category"

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45)
