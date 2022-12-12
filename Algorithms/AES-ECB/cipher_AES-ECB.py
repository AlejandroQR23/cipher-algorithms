from Crypto.Random import get_random_bytes
import time
import numpy as np
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES




for i in range(iter):
  data = b'secret'
  key = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)
  padded_block = pad(data, AES.block_size)
  T1 = time.time()
  ct_bytes = cipher.encrypt(padded_block)
  T2 = time.time()

  encryp_prom_list.append(T2 - T1)

  try:
    T1 = time.time()
    cipher = AES.new(key, AES.MODE_ECB)
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

encryp_values["AES-ECB"] = np.mean(encryp_prom_list)
encryp_prom_list.clear()

# Calculo y eliminacion de valores atipicos para la desencriptacion.
q75,q25 = np.percentile(decryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
decryp_prom_list = [i for i in decryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
decryp_prom_list = [i for i in decryp_prom_list if i > (q25 - 1.5*IQR)]

decryp_values["AES-ECB"] = np.mean(decryp_prom_list)
decryp_prom_list.clear()