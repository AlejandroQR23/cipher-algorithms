from algorithms import AES_ECB, AES_CBC, Chacha20, SHA2_384, SHA2_512, SHA3_384, SHA3_512, RSA_OAEP, RSA_PSS, ECDSA_binary, ECDSA_primes


algorithms = [
    {
        'name': 'chacha20',
        'key_size': 256,
        'description': 'ChaCha is a family of stream ciphers by Daniel J. Bernstein based on a variant of Salsa20.',
        'type': 'cipher',
        'get_avg': Chacha20.get_average_encrypt_time,
    },
    {
        'name': 'aes-ebc',
        'key_size': 256,
        'description': 'AES ECB operates with EasyDMA access to system Data RAM for in-place operations on cleartext and ciphertext during encryption.',
        'type': 'cipher',
        'get_avg': AES_ECB.get_average_encrypt_time,
    },
    {
        'name': 'aes-cbc',
        'key_size': 256,
        'description': 'CBC (short for cipher-block chaining) is a AES block cipher mode that trumps the ECB mode in hiding away patterns in the plaintext.',
        'type': 'cipher',
        'get_avg': AES_CBC.get_average_encrypt_time,
    },
    {
        'name': 'sha-2',
        'key_size': 384,
        'description': 'SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash functions designed by the United States National Security Agency (NSA) and first published in 2001.',
        'type': 'hash',
        'get_avg': SHA2_384.get_average_encrypt_time,
    },
    {
        'name': 'sha-2-512',
        'key_size': 512,
        'description': 'SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash functions designed by the United States National Security Agency (NSA) and first published in 2001.',
        'type': 'hash',
        'get_avg': SHA2_512.get_average_encrypt_time,
    },
    {
        'name': 'sha-3',
        'key_size': 384,
        'description': 'Although part of the same series of standards, SHA-3 is internally different from the MD5-like structure of SHA-1 and SHA-2.',
        'type': 'hash',
        'get_avg': SHA3_384.get_average_encrypt_time,
    },
    {
        'name': 'sha-3-512',
        'key_size': 512,
        'description': 'Although part of the same series of standards, SHA-3 is internally different from the MD5-like structure of SHA-1 and SHA-2.',
        'type': 'hash',
        'get_avg': SHA3_512.get_average_encrypt_time,
    },
    {
        'name': 'rsa-oaep',
        'key_size': 1024,
        'description': 'Optimal Asymmetric Encryption Padding (OAEP) is a padding scheme often used together with RSA encryption. OAEP was introduced by Bellare and Rogaway',
        'type': 'cipher',
        'get_avg': RSA_OAEP.get_average_encrypt_time,
    },
    {
        'name': 'rsa-pss',
        'key_size': 1024,
        'description': 'Probabilistic Signature Scheme (PSS) is a cryptographic signature scheme designed by Mihir Bellare and Phillip Rogaway.',
        'type': 'signature',
        'get_avg': RSA_PSS.get_average_encrypt_time,
    },
    {
        'name': 'ecdsa-prime',
        'key_size': 521,
        'description': ' Elliptic Curve Digital Signature Algorithm (ECDSA) offers a variant of the Digital Signature Algorithm (DSA) which uses elliptic-curve cryptography.',
        'type': 'signature',
        'get_avg': ECDSA_primes.get_average_encrypt_time,
    },
    {
        'name': 'ecdsa-binary',
        'key_size': 571,
        'description': ' Elliptic Curve Digital Signature Algorithm (ECDSA) offers a variant of the Digital Signature Algorithm (DSA) which uses elliptic-curve cryptography.',
        'type': 'signature',
        'get_avg': ECDSA_binary.get_average_encrypt_time,
    }
]
