import subprocess
from sympy.ntheory import factorint

# Variables Used
sharedPrime = 191907783019725260605646959711    # p
sharedBase = 2      # g

aliceSecret = 539727294718671     # a
bobSecret = 499314731500955      # b
# sharedPrime = 23    # p
# sharedBase = 5      # g

# aliceSecret = 6     # a
# bobSecret = 15      # b

# Begin
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

# Alice Sends Bob A = g^a mod p
A = pow(sharedBase, aliceSecret, sharedPrime)
print("Alice Sends Over Public Chanel (A): ", A)

# Bob Sends Alice B = g^b mod p
B = pow(sharedBase, bobSecret, sharedPrime)
print("Bob Sends Over Public Chanel (B): ", B)

print("\n------------\n")
print("Privately Calculated Shared Secret (S):")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = pow(B, aliceSecret, sharedPrime)
print("    Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = pow(A, bobSecret, sharedPrime)
print("    Bob Shared Secret: ", bobSharedSecret)

print("\n------------\n")
f = factorint(sharedPrime-1)
max_factor = max(f.keys())
print(max_factor)
print(
    f'python ./cado-nfs/cado-nfs.py -dlp -ell {max_factor} target={A} {sharedPrime}')
# res = subprocess.run(
#     f'python ./cado-nfs/cado-nfs.py -dlp -ell {max_factor} target={aliceSharedSecret} {sharedPrime}'.split(), capture_output=True)
# computed_client_secret = int((res.stdout.decode('utf-8').strip()))
# print(f"DLP soln: {computed_client_secret}")
log_h = 72598176602764149203650556  # from stdout
# from stderr,  same as x in the sage example
log_2 = 11263248339990185810045507


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
print(x)

p1 = pow(sharedBase, x, sharedPrime)
print(p1)
print(f'g^x=h (mod p) is {p1==A}')
# print(
#     f'python ./cado-nfs/cado-nfs.py -dlp -ell {log_h} target={sharedBase} {sharedPrime}')
