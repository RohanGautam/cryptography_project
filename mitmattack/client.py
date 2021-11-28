from utils.log_config import logging
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


class Client:
    def __init__(self) -> None:
        self.secret = 539727294718671
        self.cipher_suites = ['DHE_RSA', 'suite 2', 'suite 3']
        self.p = None
        self.g = None
        self.B = None
        self.shared_secret = None
        # for AES
        self.iv = os.urandom(16)

    def hello(self) -> list:

        log.info(
            f"client hello : offering {len(self.cipher_suites)} cipher suites")
        return self.cipher_suites

    def send_public(self):
        log.info("calculating client public paramter")
        A = pow(self.g, self.secret, self.p)
        log.info(f"A: {A}")
        return A

    def set_server_public(self, B):
        self.B = B

    def get_server_hello(self, serverhello):
        self.p, self.g, self.B = serverhello['p'], serverhello['g'], serverhello['B']

    def compute_shared_secret(self):
        log.info("calculating shared secret")
        self.shared_secret = pow(self.B, self.secret, self.p)
        log.info(f"Shared secret is {self.shared_secret}")
        # initialize AES
        key_bytes = self.shared_secret.to_bytes(32, 'big')
        self.cipher = Cipher(algorithms.AES(key_bytes),
                             modes.CBC(self.iv), backend=backend)

    def aes_encrypt(self, message):
        m = b"This is a top secret message"
        encryptor = self.cipher.encryptor()
        ct = encryptor.update(message) + encryptor.finalize()
        log.info(f'Ciphertext : {ct}')
        return ct

    def aes_decrypt(self, ciphertext):
        decryptor = self.cipher.decryptor()
        plaintext_recieved = decryptor.update(
            ciphertext) + decryptor.finalize()
        print('Decrypted plaintext : ', plaintext_recieved)
        return plaintext_recieved
