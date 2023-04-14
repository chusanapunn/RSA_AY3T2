import cryptography
import pickle

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
        return key

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(pickle.dumps(message))
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = pickle.loads(f.decrypt(encrypted_message))
    return decrypted_message

# Example usage:
generate_key()
message = {"name": "Alice", "age": 30, "city": "New York"}
encrypted_message = encrypt_message(message)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted message:", decrypted_message)