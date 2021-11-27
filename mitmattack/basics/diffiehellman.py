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
print("\n  Alice Sends Over Public Chanel: ", A)

# Bob Sends Alice B = g^b mod p
B = pow(sharedBase, bobSecret, sharedPrime)
print("Bob Sends Over Public Chanel: ", B)

print("\n------------\n")
print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = pow(B, aliceSecret, sharedPrime)
print("    Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = pow(A, bobSecret, sharedPrime)
print("    Bob Shared Secret: ", bobSharedSecret)
