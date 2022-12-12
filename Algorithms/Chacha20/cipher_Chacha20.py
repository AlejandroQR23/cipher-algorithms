from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import time
import numpy as np
from Algorithms.structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values

for i in range(iter):
  cha_plaintext = b'Texto prueba para el primer proyecto de criptografia'
  cha_key = get_random_bytes(32)
  cha_cipher = ChaCha20.new(key=cha_key)
  T1 = time.time()
  cha_ciphertext = cha_cipher.encrypt(cha_plaintext)
  T2 = time.time()

  encryp_prom_list.append(T2 - T1)

  nonce = cha_cipher.nonce

  try:
    cha_cipher = ChaCha20.new(key=cha_key, nonce=nonce)
    T1 = time.time()
    cha_plaintext_bits = cha_cipher.decrypt(cha_ciphertext)
    T2 = time.time()
  except (ValueError, KeyError):
    print("Incorrect decryption")

  decryp_prom_list.append(T2 - T1)

# Calculo y eliminacion de valores atipicos para la encriptacion.
q75,q25 = np.percentile(encryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
encryp_prom_list = [i for i in encryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
encryp_prom_list = [i for i in encryp_prom_list if i > (q25 - 1.5*IQR)]

encryp_values["Chacha20"] = np.mean(encryp_prom_list)
encryp_prom_list.clear()

# Calculo y eliminacion de valores atipicos para la desencriptacion.
q75,q25 = np.percentile(decryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
decryp_prom_list = [i for i in decryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
decryp_prom_list = [i for i in decryp_prom_list if i > (q25 - 1.5*IQR)]

decryp_values["Chacha20"] = np.mean(decryp_prom_list)
decryp_prom_list.clear()