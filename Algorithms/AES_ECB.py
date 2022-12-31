import time
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using AES-ECB"""

    encrypt_time = 0.0
    decrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)
        padded_block = pad(data, AES.block_size)

        T1 = time.time()
        cipher_message = cipher.encrypt(padded_block)
        T2 = time.time()

        encrypt_time = encrypt_time + (T2-T1)

        try:
            T1 = time.time()
            cipher.decrypt(cipher_message)
            T2 = time.time()

            decrypt_time = decrypt_time + (T2-T1)

        except (ValueError, KeyError):
            print("Incorrect decryption")

    average_encrypt_time = (encrypt_time / iterations) * 1000000
    average_decrypt_time = (decrypt_time / iterations) * 1000000

    return average_encrypt_time, average_decrypt_time
