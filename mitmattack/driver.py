from client import Client
from server import Server
from mitm import Mitm
from utils.log_config import logging

log = logging.getLogger(__name__)

log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    server = Server()
    mitm = Mitm()
    client = Client()
    server.negotiate_cipher_suite(
        mitm.forward_client_hello(
            client.hello()
        )
    )
    serverhello = mitm.forward_server_hello(
        server.hello()
    )
    p, g, B = serverhello['p'], serverhello['g'], serverhello['B']
    client.set_server_public(B)
    server.set_client_public(
        mitm.send_client_public(
            client.send_public(p, g)
        )
    )
    server.compute_shared_secret()
    client.compute_shared_secret()
