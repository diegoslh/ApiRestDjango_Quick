from typing import Self
from rest_framework.serializers import ValidationError
from modules.menus.models.menu_items import MenuItems


class MenuItemsUpdateService:

    def __init__(self: Self, *, data: dict):
        self.data = data

    def update(self: Self) -> MenuItems:
        id_menu = self.data.pop("id")
        return MenuItems.objects.filter(id=id_menu).update(**self.data)

    def inactivate(self: Self) -> int:
        id_menu = self.data.get("id")
        if not id_menu:
            raise ValidationError("ID is required")
        return MenuItems.objects.filter(id=id_menu).update(active=False)
