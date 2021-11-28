from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from utils.log_config import logging
import subprocess
from sympy.ntheory import factorint
import re

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)
backend = default_backend()


class Mitm:

    def __init__(self) -> None:
        self.secret = 15

    def forward_client_hello(self, client_hello: list) -> list:
        # TODO: raise exception if client does not offer DHE suites
        log.info("Mitm server, forwarding reuest for 1 sipher suite, DHE_RSA_EXPORT")
        return ['DHE_RSA_EXPORT']

    def forward_server_hello(self, server_hello):
        self.p, self.g, self.B = server_hello['p'], server_hello['g'], server_hello['B']
        return server_hello

    def send_client_public(self, payload):
        self.A = payload
        return payload

    def compute_shared_secret(self):
        f = factorint(self.p-1)
        max_factor = max(f.keys())
        log.info(
            f'CADO NFS, running : python ./cado-nfs/cado-nfs.py -dlp -ell {max_factor} target={self.A} {self.p}')
        res = subprocess.run(
            f'python ./cado-nfs/cado-nfs.py -dlp -ell {max_factor} target={self.A} {self.p}'.split(), capture_output=True)
        log_h = int((res.stdout.decode('utf-8').strip()))
        log_2 = int(re.search(r'log2 = (\d*)',
                    res.stderr.decode('utf-8')).group(1))

        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)

        def modinv(a, m):
            g, x, y = egcd(a, m)
            if g != 1:
                raise Exception('modular inverse does not exist')
            else:
                return x % m
        x = (log_h*modinv(log_2, max_factor)) % max_factor

        log.info(f'Client\'s secret: {x}')
        assert pow(self.g, x, self.p) == self.A
        # compute shared secret
        self.S = pow(self.B, x, self.p)

    def forward_client_to_server(self, ciphertext, iv):
        cipher = Cipher(algorithms.AES(self.S.to_bytes(32, 'big')),
                        modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        plaintext_recieved = (decryptor.update(
            ciphertext) + decryptor.finalize()).decode('utf-8')
        log.info(f'MITM Decrypted plaintext : {plaintext_recieved}')
        return ciphertext
