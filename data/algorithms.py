from algorithms import AES_ECB


algorithms = [
    {
        'name': 'chacha20',
        'key_size': 256,
        'description': 'test',
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
        'description': ''
    },
    {
        'name': 'sha-2',
        'key_size': 384,
        'description': ''
    },
    {
        'name': 'sha-2-512',
        'key_size': 512,
        'description': ''
    },
    {
        'name': 'sha-3',
        'key_size': 384,
        'description': ''
    },
    {
        'name': 'sha-3-512',
        'key_size': 512,
        'description': ''
    },
    {
        'name': 'rsa-oaep',
        'key_size': 1024,
        'description': ''
    },
    {
        'name': 'rsa-pss',
        'key_size': 1024,
        'description': ''
    },
    {
        'name': 'ecdsa-prime',
        'key_size': 521,
        'description': ''
    },
    {
        'name': 'ecdsa-binary',
        'key_size': 571,
        'description': ''
    }
]

# TODO: Add description to each algorithm

# TODO: Add category to each algorithm (hash, cipher, signature, etc)
