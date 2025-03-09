from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from typing import Self
from modules.shared.utilities.utilities import response_paginate
from modules.users.models.user import User
from modules.users.selectors.user import UserSelector
from modules.users.filters.user import UserFilter
from modules.users.serializers.user import (
    UserSerializer,
    UserUpdateSerializer,
    UserCreateSerializer,
)
from modules.users.services.user_create import UserCreateService
from modules.users.services.user_update import UserUpdateService


class UserAPIView(APIView):

    def get(self: Self, request: Request) -> Response:
        queryset: QuerySet = UserSelector.get_all_users()
        filters: QuerySet[User] = UserFilter(request.query_params, queryset=queryset).qs
        serializer = UserSerializer(filters, many=True).data
        return response_paginate(request=request, data=serializer)

    def post(self: Self, request: Request) -> Response:
        serializer: UserCreateSerializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserCreateService(data=serializer.validated_data).create()
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED,
        )

    def patch(self: Self, request: Request) -> Response:
        menu_id = request.query_params.get("id")
        data = {"id": menu_id, **request.data}
        serializer = UserUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        UserUpdateService(data=serializer.validated_data).update()
        return Response(
            {"message": "User updated successfully"},
            status=status.HTTP_200_OK,
        )

    def delete(self: Self, request: Request) -> Response:
        menu_id = request.query_params.get("id")
        UserUpdateService(data={"id": menu_id}).inactivate()
        return Response(
            {"message": "User deleted successfully"},
            status=status.HTTP_200_OK,
        )
