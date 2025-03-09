from django.db.models import QuerySet
from modules.users.models.user import User


class UserSelector:

    def get_all_users() -> QuerySet[User]:
        # return User.objects.filter(active=True).order_by("-id")
        return (
            User.objects.filter(active=True)
            .select_related("restaurant_id")
            .order_by("-id")
        )

    def get_user_by_id(id) -> User:
        return User.objects.filter(id=id, active=True).first()
