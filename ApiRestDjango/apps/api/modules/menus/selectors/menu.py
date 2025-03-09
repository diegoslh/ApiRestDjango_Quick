from django.db.models import QuerySet
from modules.menus.models.menu_items import MenuItems
from modules.menus.models.menu_category import MenuCategory


class MenuSelector:
    def get_all_menus() -> QuerySet[MenuItems]:
        return (
            MenuItems.objects.filter(active=True)
            .select_related("restaurant_id", "category_id")
            .order_by("-id")
        )

    def get_menu_by_id(id) -> MenuItems:
        return MenuItems.objects.filter(id=id, active=True).first()

    def get_all_categories() -> QuerySet[MenuCategory]:
        return MenuCategory.objects.filter(active=True).order_by("-id")
