import time
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using RSA-OAEP"""

    if iterations > 1:
        raise ValueError("Iterations must be 1")

    encrypt_time = 0.0
    decrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        keys = RSA.generate(2048)
        public_key = keys.publickey()

        cipher = PKCS1_OAEP.new(public_key)

        T1 = time.time()
        cipher_message = cipher.encrypt(data)
        T2 = time.time()

        encrypt_time += (T2-T1)

        cipher = PKCS1_OAEP.new(keys)

        T1 = time.time()
        cipher.decrypt(cipher_message)
        T2 = time.time()

        decrypt_time += (T2-T1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations
    average_decrypt_time = (decrypt_time * 1000000) / iterations

    return average_encrypt_time, average_decrypt_time
