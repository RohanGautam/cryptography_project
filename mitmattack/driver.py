from client import Client
from server import Server
from mitm import Mitm


if __name__ == '__main__':
    server = Server()
    mitm = Mitm()
    client = Client()
    print(
        server.negotiate_cipher_suite(
            mitm.forward_hello(
                client.hello()
            )
        )
    )
