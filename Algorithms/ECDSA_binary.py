import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def get_average_encrypt_time(iterations, data):
    """
    Returns the average time in microseconds to sign and verify a block of data using ECDSA
    """

    if iterations > 50:
        raise ValueError("Iterations must be less than 50")

    signing_time = 0.0
    verification_time = 0.0

    data = data.encode()

    for _ in range(iterations):
        private_key = ec.generate_private_key(ec.SECT571K1())
        public_key = private_key.public_key()

        T1 = time.time()
        sign = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        T2 = time.time()

        signing_time = signing_time + (T2-T1)

        T1 = time.time()
        public_key.verify(sign, data, ec.ECDSA(hashes.SHA256()))
        T2 = time.time()

        verification_time = verification_time + (T2-T1)

    average_signing_time = (signing_time * 1000000) / iterations
    average_verification_time = (verification_time * 1000000) / iterations

    return average_signing_time, average_verification_time
