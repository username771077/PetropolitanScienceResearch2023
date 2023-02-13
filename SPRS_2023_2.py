import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Crypto.PublicKey import RSA

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, public_key):
    key = RSA.import_key(public_key)
    aes_key = os.urandom(32)
    encrypted_aes_key = key.encrypt(aes_key, 32)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(aes_key), modes.GCM(b'\0' * 12), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(message) + encryptor.finalize()
    return encrypted_aes_key, encrypted_data

def decrypt_message(encrypted_aes_key, encrypted_data, private_key):
    key = RSA.import_key(private_key)
    aes_key = key.decrypt(encrypted_aes_key)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(aes_key), modes.GCM(b'\0' * 12), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data

