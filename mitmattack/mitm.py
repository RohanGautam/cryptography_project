from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from utils.log_config import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)
backend = default_backend()


class Mitm:

    def __init__(self) -> None:
        self.secret = 15

    def forward_client_hello(self, client_hello: list) -> list:
        # TODO: raise exception if client does not offer DHE suites
        log.info("Mitm server, forwarding reuest for 1 sipher suite, DHE_RSA_EXPORT")
        return ['DHE_RSA_EXPORT']

    def forward_server_hello(self, server_hello):
        return server_hello

    def send_client_public(self, payload):
        return payload

    def forward_client_to_server(self, ciphertext, S, iv):
        cipher = Cipher(algorithms.AES(S.to_bytes(32, 'big')),
                        modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        plaintext_recieved = (decryptor.update(
            ciphertext) + decryptor.finalize()).decode('utf-8')
        log.info(f'MITM Decrypted plaintext : {plaintext_recieved}')
        return ciphertext
