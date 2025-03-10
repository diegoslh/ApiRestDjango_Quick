from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from typing import Self
from modules.users.models import User
from modules.authentication.serializer.authentication import AuthenticationSerializer
from modules.authentication.services.login import LoginService
from modules.authentication.DTOs.authentication import AuthenticationDTO


class AuthenticationAPIView(APIView):

    def post(self: Self, request: Request) -> Response:
        serializer: AuthenticationSerializer = AuthenticationSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user: User = LoginService(data=serializer.validated_data).validate_credentials()
        user_dto = AuthenticationDTO(user).data()

        return Response(
            {
                "message": "Login successful !!",
                "user_data": user_dto,
                "token": LoginService.create_token(user_data=user_dto),
            },
            status=status.HTTP_200_OK,
        )
