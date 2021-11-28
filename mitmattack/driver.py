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

    # client hello to server
    server.negotiate_cipher_suite(
        mitm.forward_client_hello(
            client.hello()
        )
    )

    # server hello to client, with server public params
    client.get_server_hello(
        mitm.forward_server_hello(
            server.hello()
        )
    )

    # exchange public parameters of client
    server.set_client_public(
        mitm.send_client_public(
            client.send_public()
        )
    )
    # server and client compute shared secret
    server.compute_shared_secret()
    client.compute_shared_secret()
    # the mitm server computes the shared secret by solving the DLP
    mitm.compute_shared_secret()

    # share client AES IV with server (public)
    server.init_aes(client.iv)
    # An example of AES interception by the MITM server.
    server.parse_client_msg(
        mitm.forward_client_to_server(
            client.aes_encrypt("a secret message".encode()),
            client.iv
        )
    )
