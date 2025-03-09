from cryptography.fernet import Fernet

# Generar una clave de cifrado
new_key = Fernet.generate_key()
ciphered = Fernet(new_key)


class EncryptionService:
    @staticmethod
    def encrypt_password(raw_password: str) -> bytes:
        return ciphered.encrypt(raw_password.encode())

    @staticmethod
    def decrypt_password(encrypted_password: bytes) -> str:
        return ciphered.decrypt(encrypted_password).decode()

    @staticmethod
    def verify_password(raw_password: str, encrypted_password: bytes) -> bool:
        return EncryptionService.decrypt_password(encrypted_password) == raw_password
