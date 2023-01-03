import time
from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES


def encrypt(data, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_data = cipher.encrypt(pad(data, AES.block_size))
    return b64encode(iv + cipher_data)


def decrypt(key, data):
    raw = b64decode(data)
    cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using AES-CBC"""

    encrypt_time = 0.0
    decrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        key = get_random_bytes(16)

        T1 = time.time()
        cipher_message = encrypt(data, key)
        T2 = time.time()

        encrypt_time += (T2-T1)

        T1 = time.time()
        decrypt(key, cipher_message)
        T2 = time.time()

        decrypt_time += (T2-T1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations
    average_decrypt_time = (decrypt_time * 1000000) / iterations

    return average_encrypt_time, average_decrypt_time
