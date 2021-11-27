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

    def negotiate_cipher_suite(self, suites: list) -> str:
        if all([s not in self.supported_suites for s in suites]):
            raise Exception("No supported cipher suites found")
        supported_and_present = [(suite, priority)
                                 for suite, priority in self.supported_suites.items() if suite in suites]
        chosen_suite = sorted(supported_and_present, key=lambda x: x[0])[0][0]
        return chosen_suite

    def hello(self):
        print('moo')
