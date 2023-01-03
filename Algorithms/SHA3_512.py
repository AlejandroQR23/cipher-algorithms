import time
from Crypto.Hash import SHA3_512


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using SHA-3_512"""

    encrypt_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        hash_sha3_512 = SHA3_512.new(data)

        t1 = time.time()
        hash_sha3_512.update(b"update")
        t2 = time.time()

        encrypt_time += (t2-t1)

    average_encrypt_time = (encrypt_time * 1000000) / iterations

    return average_encrypt_time, None
