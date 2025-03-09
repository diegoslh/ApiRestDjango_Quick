import django_filters
from modules.users.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = "__all__"
