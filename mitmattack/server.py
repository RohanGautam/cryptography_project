import random
from utils.log_config import logging
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


class Server:
    # prime = 23
    # base = 5
    # 196 bit
    prime = 191907783019725260605646959711
    base = 2

    def __init__(self) -> None:
        # random.getrandbits(98)
        self.secret = 499314731500955
        self.supported_suites = {
            'suite 1': 1,
            'DHE_RSA': 2,
            'suite 2': 3,
            'suite 3': 4,
            'suite 4': 5,
            'DHE_RSA_EXPORT': 6
        }
        self.chosen_suite = 'suite 1'  # highest priority
        self.A = None

    def negotiate_cipher_suite(self, suites: list) -> str:
        log.info(
            f"server negotiating cipher suite. Client supports the following suites:{suites}")
        if all([s not in self.supported_suites for s in suites]):
            raise Exception("No supported cipher suites found")
        supported_and_present = [(suite, priority)
                                 for suite, priority in self.supported_suites.items() if suite in suites]
        chosen_suite = sorted(supported_and_present, key=lambda x: x[0])[0][0]
        self.chosen_suite = chosen_suite
        return chosen_suite

    def hello(self):
        log.info("calculating server public parameter")
        payload = {
            'ciphersuite': self.chosen_suite,
            'p': self.prime,
            'g': self.base,
            'B': pow(self.base, self.secret, self.prime)
        }
        log.info(f"B: {payload['B']}")
        return payload

    def set_client_public(self, A):
        self.A = A

    def compute_shared_secret(self):
        log.info("calculating shared secret")
        self.shared_secret = pow(self.A, self.secret, self.prime)
        log.info(f"Shared secret is {self.shared_secret}")

    def init_aes(self, iv):
        key_bytes = self.shared_secret.to_bytes(32, 'big')
        self.cipher = Cipher(algorithms.AES(key_bytes),
                             modes.CBC(iv), backend=backend)

    def parse_client_msg(self, ciphertext):
        decryptor = self.cipher.decryptor()
        plaintext_recieved = (decryptor.update(
            ciphertext) + decryptor.finalize()).decode('utf-8')
        log.info(f'Server Decrypted plaintext : {plaintext_recieved}')
        return ciphertext
