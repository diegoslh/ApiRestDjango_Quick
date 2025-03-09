from typing import Self
from modules.menus.models.menu_items import MenuItems


class MenuItemsCreateService:

    def __init__(self: Self, *, data: dict):
        self.data = data

    def create(self: Self) -> MenuItems:
        return MenuItems.objects.create(**self.data)
