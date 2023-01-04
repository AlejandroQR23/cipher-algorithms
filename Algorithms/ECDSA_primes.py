import time
from ecdsa import SigningKey, NIST521p


def get_average_encrypt_time(iterations, data):
    """
    Returns the average time in microseconds to sign and verify a block of data using ECDSA
    """

    if iterations > 50:
        raise ValueError("Iterations must be less than 50")

    verification_time = 0.0
    signature_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        private_key = SigningKey.generate(curve=NIST521p)
        publick_key = private_key.verifying_key

        T1 = time.time()
        sign = private_key.sign(data)
        T2 = time.time()

        signature_time = signature_time + (T2-T1)

        T1 = time.time()
        publick_key.verify(sign, data)
        T2 = time.time()

        verification_time = verification_time + (T2-T1)

    average_signature_time = (signature_time * 1000000) / iterations
    average_verification_time = (verification_time * 1000000) / iterations

    return average_signature_time, average_verification_time
