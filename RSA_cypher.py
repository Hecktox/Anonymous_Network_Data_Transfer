import random
import math


class RSA_cypher:
    def __init__(self, nodeId):
        self.nodeId = nodeId

    def is_prime(self, n, k=5):
        """
        Miller-Rabin primality test. Returns True if n is probably prime.
        """
        if n <= 1 or n % 2 == 0:
            return False
        if n == 2:
            return True

        # Write n as d*2^r + 1
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Witness loop
        for _ in range(k):
            a = random.randint(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_prime(self, bits):
        """
        Generate a random prime number with the specified number of bits.
        """
        while True:
            candidate = random.getrandbits(bits)
            if self.is_prime(candidate):
                return candidate

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def generate_keypair(self, bits):
        p = self.generate_prime(bits)
        q = self.generate_prime(bits)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randint(2, phi - 1)
        while self.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)

        d = self.modinv(e, phi)

        return ((n, e), (n, d))

    def encrypt(self, message, public_key):
        if type(public_key) is str:
            pubSet = public_key.replace("(", "").replace(")", "").strip().split(", ")
            public_key = (int(pubSet[0]), int(pubSet[1]))

        n, e = public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message

    def decrypt(self, encrypted_message, private_key):
        n, d = private_key
        decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
        return decrypted_message

    def setup_keys_for_node(self):
        keypair = self.generate_keypair(bits=16)
        public_key, private_key = keypair

        # print(type(public_key))

        print(f"Public Key (n, e): {public_key}")
        print(f"Private Key (n, d): {private_key}")

        with open(f"keys\\node{self.nodeId}pub.txt", "w+") as file:
            file.write(f"{public_key}")
        with open(f"keys\\node{self.nodeId}priv.txt", "w+") as file:
            file.write(f"{private_key}")

    def get_public_key(self):
        with open(f"keys\\node{self.nodeId}pub.txt", "r") as file:
            pubSet = file.readline().replace("(", "").replace(")", "").strip().split(", ")
            public_key = (int(pubSet[0]), int(pubSet[1]))
            return public_key

    def get_private_key(self):
        with open(f"keys\\node{self.nodeId}priv.txt", "r") as file:
            privSet = file.readline().replace("(", "").replace(")", "").strip().split(", ")
            private_key = (int(privSet[0]), int(privSet[1]))
            return private_key

    def get_keys(self):
        public_key = self.get_public_key()
        private_key = self.get_private_key()

        return public_key, private_key


if __name__ == "__main__":

    print("hey")
    # nodeId = 6
    # cypherClient = RSA_cypher(nodeId)
    # keypair = cypherClient.generate_keypair(bits=16)
    # public_key, private_key = keypair
    #
    # print(type(public_key))
    #
    # print(f"Public Key (n, e): {public_key}")
    # print(f"Private Key (n, d): {private_key}")
    #
    # with open(f"keys\\node{nodeId}pub.txt", "w+") as file:
    #     file.write(f"{public_key}")
    # with open(f"keys\\node{nodeId}priv.txt", "w+") as file:
    #     file.write(f"{private_key}")

    # with open(f"keys\\node{nodeId}pub.txt", "r") as file:
    #     pubSet = file.readline().replace("(", "").replace(")", "").strip().split(", ")
    #     public_key = (int(pubSet[0]), int(pubSet[1]))
    # with open(f"keys\\node{nodeId}priv.txt", "r") as file:
    #     privSet = file.readline().replace("(", "").replace(")", "").strip().split(", ")
    #     private_key = (int(privSet[0]), int(privSet[1]))
    #
    #     print(type(public_key))

    # print(f"Public Key (n, e): {public_key}")
    # print(f"Private Key (n, d): {private_key}")



    # setup_keys_for_node(1)
    #
    # public_key, private_key = get_keys(1)
    #
    # # Example usage
    # message = "Hello, RSA!"
    # # public_key = (n, e)  # Replace with your actual public key
    # # private_key = (n, d)  # Replace with your actual private key
    #
    # # Encrypt the message
    # encrypted_message = encrypt(message, public_key)
    # print(f"Encrypted Message: {encrypted_message}")
    #
    # # Decrypt the message
    # decrypted_message = decrypt(encrypted_message, private_key)
    # print(f"Decrypted Message: {decrypted_message}")
