# listas que contendran los promedios de los algorimos a probar
encryp_prom_list = []
decryp_prom_list = []
hash_prom_list = []
sign_prom_list = []
verify_prom_list = []

# Diccionarios que almacenaran promedios
encryp_values = { "Chacha20": 0, "AES-ECB": 0, "AES-GCM": 0, "RSA-OAEP": 0 }
decryp_values = { "Chacha20": 0, "AES-ECB": 0, "AES-GCM": 0, "RSA-OAEP": 0 }
hash_values = { "SHA2-384": 0, "SHA2-512": 0, "SHA3-384": 0, "SHA3-512": 0 }
sign_values = { "RSA-PSS": 0, "ECDSA PF": 0, "ECDSA BF": 0 }
verify_values = { "RSA-PSS": 0, "ECDSA PF": 0, "ECDSA BF": 0 }