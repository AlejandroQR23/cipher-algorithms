from algorithms import AES_ECB, AES_CBC, Chacha20, SHA2_384, SHA2_512, SHA3_384, SHA3_512, RSA_OAEP, RSA_PSS, ECDSA_binary, ECDSA_primes


algorithms = [
    {
        'name': 'chacha20',
        'key_size': 256,
        'description': '',
        'get_avg': Chacha20.get_average_encrypt_time,
    },
    {
        'name': 'aes-ebc',
        'key_size': 256,
        'description': '',
        'get_avg': AES_ECB.get_average_encrypt_time,
    },
    {
        'name': 'aes-cbc',
        'key_size': 256,
        'description': '',
        'get_avg': AES_CBC.get_average_encrypt_time,
    },
    {
        'name': 'sha-2',
        'key_size': 384,
        'description': '',
        'get_avg': SHA2_384.get_average_encrypt_time,
    },
    {
        'name': 'sha-2-512',
        'key_size': 512,
        'description': '',
        'get_avg': SHA2_512.get_average_encrypt_time,
    },
    {
        'name': 'sha-3',
        'key_size': 384,
        'description': '',
        'get_avg': SHA3_384.get_average_encrypt_time,
    },
    {
        'name': 'sha-3-512',
        'key_size': 512,
        'description': '',
        'get_avg': SHA3_512.get_average_encrypt_time,
    },
    {
        'name': 'rsa-oaep',
        'key_size': 1024,
        'description': '',
        'get_avg': RSA_OAEP.get_average_encrypt_time,
    },
    {
        'name': 'rsa-pss',
        'key_size': 1024,
        'description': '',
        'get_avg': RSA_PSS.get_average_encrypt_time,
    },
    {
        'name': 'ecdsa-prime',
        'key_size': 521,
        'description': '',
        'get_avg': ECDSA_primes.get_average_encrypt_time,
    },
    {
        'name': 'ecdsa-binary',
        'key_size': 571,
        'description': '',
        'get_avg': ECDSA_binary.get_average_encrypt_time,
    }
]

# TODO: Add description to each algorithm

# TODO: Add category to each algorithm (hash, cipher, signature, etc)
