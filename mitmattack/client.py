class Client:
    def __init__(self) -> None:
        self.secret = 6

    def hello(self) -> list:
        return ['DHE_RSA', 'suite 2', 'suite 3']
