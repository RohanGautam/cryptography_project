from utils.log_config import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


class Server:
    prime = 23
    base = 5

    def __init__(self) -> None:
        self.secret = 15
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
        payload = {
            'ciphersuite': self.chosen_suite,
            'p': self.prime,
            'g': self.base,
            'B': (self.base**self.secret) % self.prime
        }
        log.info(f"sending payload: {payload}")
        return payload

    def set_client_public(self, A):
        self.A = A

    def compute_shared_secret(self):
        self.shared_secret = (self.A**self.secret) % self.prime
        log.info(f"Shared secret is {self.shared_secret}")
