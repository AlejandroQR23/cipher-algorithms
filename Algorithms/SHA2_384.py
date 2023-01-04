import time
import numpy as np
from Crypto.Hash import SHA384


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using AES-ECB"""
    encrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        sha2_hash = SHA384.new(data)
        t1 = time.time()
        sha2_hash.update(b"update")
        t2 = time.time()

        encrypt_time += (t2-t1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations

    return average_encrypt_time, None
