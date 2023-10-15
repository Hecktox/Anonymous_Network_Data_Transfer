import random

#Checks if a given number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Generates large number and then checks if it is prime
def generate_large_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1
        if is_prime(candidate):
            return candidate

#Calculates greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#This function calculates the multiplicative inverse of 'e' modulo 'phi'.
# It checks if 'e' and 'phi' are coprime (their GCD is 1) and then uses
# the extended Euclidean algorithm to find the modular multiplicative inverse of 'e' modulo 'phi'.
def multiplicative_inverse(e, phi):
    if gcd(e, phi) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phi

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1,
            u2 - q * v2,
            u3 - q * v3,
            v1,
            v2,
            v3,
        )

    return u1 % phi

#Encrypts msg using the RSA algorithm.Takes each character as ASCII and encrypts 
def rsa_encrypt(plaintext, public_key, modulus):
    encrypted = [pow(ord(char), public_key, modulus) for char in plaintext]
    return encrypted

def rsa_decrypt(ciphertext, private_key, modulus):
    decrypted = [chr(pow(char, private_key, modulus)) for char in ciphertext]
    return ''.join(decrypted)

# Generate large primes
p = generate_large_prime(32)
q = generate_large_prime(32)

# Calculate modulus and totient
n = p * q
phi = (p - 1) * (q - 1)

# Choose an encryption key (e) and compute the decryption key (d)
e = 65537  # commonly used value for e
d = multiplicative_inverse(e, phi)

# Example usage for encryption and decryption
message = "Hello, this is a secret message."
print(f"Original message: {message}")

# Encrypt the message
encrypted_message = rsa_encrypt(message, e, n)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = rsa_decrypt(encrypted_message, d, n)
print(f"Decrypted message: {decrypted_message}")