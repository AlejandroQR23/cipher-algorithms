import time
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

for i in range(iter):
  message = b'To be signed'
  keys = RSA.generate(2048)
  private_key = keys.export_key()
  public_key = keys.publickey()

  h = SHA256.new(message)

  T1 = time.time()
  signature = pss.new(keys).sign(h)
  T2 = time.time()

  sign_prom_list.append( T2 - T1 )

  verifier = pss.new(keys)
  try:
    T1 = time.time()
    verifier.verify(h, signature)
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except (ValueError, TypeError):
    print ("The signature is not authentic.")

# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(sign_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
sign_prom_list = [i for i in sign_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
sign_prom_list = [i for i in sign_prom_list if i > (q25 - 1.5*IQR)]

sign_values["RSA-PSS"] = np.mean(sign_prom_list)
sign_prom_list.clear()


# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(verify_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
verify_prom_list = [i for i in verify_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
verify_prom_list = [i for i in verify_prom_list if i > (q25 - 1.5*IQR)]

verify_values["RSA-PSS"] = np.mean(verify_prom_list)
verify_prom_list.clear()