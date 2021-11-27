class Mitm:

    def __init__(self) -> None:
        self.secret = 15

    def forward_hello(self, client_hello: list) -> list:
        return ['DHE_RSA_EXPORT']
