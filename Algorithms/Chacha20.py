from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import time


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using ChaCha20"""

    encrypt_time = 0.0
    decrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        key = get_random_bytes(32)
        cipher = ChaCha20.new(key=key)

        t1 = time.time()
        ciphertext = cipher.encrypt(data)
        t2 = time.time()

        encrypt_time = encrypt_time+(t2-t1)

        nonce = cipher.nonce
        decipher = ChaCha20.new(key=key, nonce=nonce)
        t1 = time.time()
        decipher.decrypt(ciphertext)
        t2 = time.time()

        decrypt_time = decrypt_time+(t2-t1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations
    average_decrypt_time = (decrypt_time * 1000000) / iterations

    return average_encrypt_time, average_decrypt_time
