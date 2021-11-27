from utils.log_config import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


class Client:
    def __init__(self) -> None:
        self.secret = 6
        self.cipher_suites = ['DHE_RSA', 'suite 2', 'suite 3']
        self.p = None
        self.g = None
        self.B = None
        self.shared_secret = None

    def hello(self) -> list:

        log.info(
            f"client hello : offering {len(self.cipher_suites)} cipher suites")
        return self.cipher_suites

    def send_public(self, p, g):
        self.p = p
        self.g = g
        return (g**self.secret) % p

    def set_server_public(self, B):
        self.B = B

    def compute_shared_secret(self):
        self.shared_secret = (self.B**self.secret) % self.p
        log.info(f"Shared secret is {self.shared_secret}")
