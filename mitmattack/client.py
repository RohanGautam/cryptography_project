from utils.log_config import logging
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

    def hello(self) -> list:

        log.info(
            f"client hello : offering {len(self.cipher_suites)} cipher suites")
        return self.cipher_suites

    def send_public(self, p, g):
        self.p = p
        self.g = g
        log.info("calculating client public paramter")
        A = pow(g, self.secret, p)
        log.info(f"A: {A}")
        return A

    def set_server_public(self, B):
        self.B = B

    def compute_shared_secret(self):
        log.info("calculating shared secret")
        self.shared_secret = pow(self.B, self.secret, self.p)
        log.info(f"Shared secret is {self.shared_secret}")
