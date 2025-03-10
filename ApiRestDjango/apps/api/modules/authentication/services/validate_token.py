import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


def validate_token(*, request: Request) -> None:

    token = request.headers.get("Authorization", "").split("Bearer ")[-1]
    if not token:
        raise AuthenticationFailed("Authorization token not provided")

    try:
        jwt.decode(token, "OUH85S", algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token has expired")

    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Invalid token")
