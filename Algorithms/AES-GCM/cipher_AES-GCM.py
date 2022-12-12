from Crypto.Random import get_random_bytes
import time
import numpy as np
from Crypto.Cipher import AES





for i in range(iter):
  header = b"header"
  data = b"secret"
  aes_gcm_key = get_random_bytes(16)
  aes_gcm_cipher = AES.new(aes_gcm_key, AES.MODE_GCM)
  aes_gcm_cipher.update(header)
  T1 = time.time()
  aes_gcm_ciphertext, tag = aes_gcm_cipher.encrypt_and_digest(data)
  T2 = time.time()

  encryp_prom_list.append(T2 - T1)

  nonce = aes_gcm_cipher.nonce

  try:
      aes_gcm_cipher = AES.new(aes_gcm_key, AES.MODE_GCM, nonce)
      aes_gcm_cipher.update(header)
      T1 = time.time()
      plaintext = aes_gcm_cipher.decrypt_and_verify(aes_gcm_ciphertext, tag)
      T2 = time.time()
      decryp_prom_list.append(T2 - T1)
  except (ValueError, KeyError):
      print("Incorrect decryption")

# Calculo y eliminacion de valores atipicos para la encriptacion.
q75,q25 = np.percentile(encryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
encryp_prom_list = [i for i in encryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
encryp_prom_list = [i for i in encryp_prom_list if i > (q25 - 1.5*IQR)]

encryp_values["AES-GCM"] = np.mean(encryp_prom_list)
encryp_prom_list.clear()

# Calculo y eliminacion de valores atipicos para la desencriptacion.
q75,q25 = np.percentile(decryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
decryp_prom_list = [i for i in decryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
decryp_prom_list = [i for i in decryp_prom_list if i > (q25 - 1.5*IQR)]

decryp_values["AES-GCM"] = np.mean(decryp_prom_list)
decryp_prom_list.clear()