from utils.log_config import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)


class Client:
    def __init__(self) -> None:
        self.secret = 6
        self.cipher_suites = ['DHE_RSA', 'suite 2', 'suite 3']

    def hello(self) -> list:

        log.info(
            f"client hello : offering {len(self.cipher_suites)} cipher suites")
        return self.cipher_suites
