from cryptography.fernet import Fernet
from django.conf import settings

# Generar una clave de cifrado
key = settings.ENCRYPTION_KEY.encode()
ciphered = Fernet(key)


class EncryptionService:
    @staticmethod
    def encrypt_password(password: str) -> bytes:
        return ciphered.encrypt(password.encode())

    @staticmethod
    def decrypt_password(encrypted_password: bytes) -> str:
        return ciphered.decrypt(encrypted_password).decode()

    @staticmethod
    def verify_password(password: str, encrypted_password: bytes) -> bool:
        try:
            decrypted_password = EncryptionService.decrypt_password(
                encrypted_password
            )
            return decrypted_password == password
        except Exception:
            return False
