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
    A = client.send_public(p, g)
    server.set_client_public(
        mitm.send_client_public(
            A
        )
    )
    server.compute_shared_secret()
    client.compute_shared_secret()
    # NFS commands
    # Get the largest primes:
    # res = subprocess.run(
    #     f'python ./cado-nfs/cado-nfs.py {p} -t all'.split(), capture_output=True)
    # # largest prime factor of p-1
    # print(res.stdout.decode('utf-8'))
    # largest_prime_factor = max([int(x)
    #                            for x in res.stdout.decode('utf-8').split()])
    # log.info(f"largest prime factor of p-1: {largest_prime_factor}")
    # log.info('Calculating client secret')
    # res = subprocess.run(
    #     f'python ./cado-nfs/cado-nfs.py -dlp -ell {largest_prime_factor} target={A} {p}'.split(), capture_output=True)
    # computed_client_secret = int((res.stdout.decode('utf-8').strip()))
    # log.info(f"DLP soln: {computed_client_secret}")
    # if computed_client_secret != client.secret:
    #     log.error(
    #         f"DOES NOT MATCH: {computed_client_secret} != {client.secret}")
