import django_filters
from modules.menus.models.menu_items import MenuItems


class MenuItemsFilter(django_filters.FilterSet):
    class Meta:
        model = MenuItems
        fields = "__all__"
