import subprocess
from client import Client
from server import Server
from mitm import Mitm
from utils.log_config import logging
import subprocess

log = logging.getLogger(__name__)

log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    server = Server()
    mitm = Mitm()
    client = Client()

    # client hello
    server.negotiate_cipher_suite(
        mitm.forward_client_hello(
            client.hello()
        )
    )
    client.get_server_hello(
        mitm.forward_server_hello(
            server.hello()
        )
    )
    # p, g, B = serverhello['p'], serverhello['g'], serverhello['B']
    # client.set_server_public(B)

    server.set_client_public(
        mitm.send_client_public(
            client.send_public()
        )
    )
    server.compute_shared_secret()
    client.compute_shared_secret()
    # the special part
    mitm.compute_shared_secret()

    S = client.shared_secret
    server.init_aes(client.iv)  # publicly known, so share freely
    server.parse_client_msg(
        mitm.forward_client_to_server(
            client.aes_encrypt("a secret message".encode()),
            client.iv
        )
    )
