import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

key = os.urandom(32)  # private
iv = os.urandom(16)  # publicly known
plaintext_sent = b"a secret message"
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(plaintext_sent) + encryptor.finalize()
print('Ciphertext : ', ct)
decryptor = cipher.decryptor()
plaintext_recieved = decryptor.update(ct) + decryptor.finalize()
print('Decrypted plaintext : ', plaintext_recieved)
