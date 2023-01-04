import time
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256


def get_average_encrypt_time(iterations, data):
    """Returns the average time in microseconds to encrypt a block of data using RSA-PSS"""

    if iterations > 5:
        raise ValueError("Iterations must be less than 6")

    signing_time = 0.0
    verification_time = 0.0

    message = data.encode()

    keys = RSA.generate(2048)

    for _ in range(iterations):
        keys.export_key()
        keys.publickey()

        h = SHA256.new(message)
        T1 = time.time()
        signature = pss.new(keys).sign(h)
        T2 = time.time()
        signing_time = signing_time + (T2-T1)

        verifier = pss.new(keys)
        T1 = time.time()
        verifier.verify(h, signature)
        T2 = time.time()

        verification_time = verification_time + (T2-T1)

    average_signing_time = (signing_time * 1000000) / iterations
    average_verification_time = (verification_time * 1000000) / iterations

    return average_signing_time, average_verification_time
