import time
import numpy as np
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA





for i in range(iter):
  message = b'You can attack now!'
  keys = RSA.generate(2048)
  public_key = keys.publickey()

  cipher = PKCS1_OAEP.new(public_key)
  T1 = time.time()
  ciphertext = cipher.encrypt(message)
  T2 = time.time()

  encryp_prom_list.append(T2 - T1)

  try:
    cipher = PKCS1_OAEP.new(keys)
    T1 = time.time()
    message = cipher.decrypt(ciphertext)
    T2 = time.time()
    decryp_prom_list.append(T2 - T1)
  except(ValueError, TypeError):
    print("Incorrect decryption")
  
# Calculo y eliminacion de valores atipicos para la encriptacion.
q75,q25 = np.percentile(encryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
encryp_prom_list = [i for i in encryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
encryp_prom_list = [i for i in encryp_prom_list if i > (q25 - 1.5*IQR)]

encryp_values["RSA-OAEP"] = np.mean(encryp_prom_list)
encryp_prom_list.clear()

# Calculo y eliminacion de valores atipicos para la desencriptacion.
q75,q25 = np.percentile(decryp_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
decryp_prom_list = [i for i in decryp_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
decryp_prom_list = [i for i in decryp_prom_list if i > (q25 - 1.5*IQR)]

decryp_values["RSA-OAEP"] = np.mean(decryp_prom_list)
decryp_prom_list.clear()