import time
import numpy as np
from Crypto.Hash import SHA3_384


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using SHA-3-384"""

    encrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        cipher = SHA3_384.new(data)
        t1 = time.time()
        cipher.update(b"update")
        t2 = time.time()

        encrypt_time += (t2-t1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations

    return average_encrypt_time, None
