import time
import numpy as np
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from Algorithms.structures import sign_prom_list,verify_prom_list,sign_values,verify_values

for i in range(iter):
  llaveFirmaPrivada = ec.generate_private_key(ec.SECT571K1())
  llavePublica = llaveFirmaPrivada.public_key()

  T1 = time.time()
  firma = llaveFirmaPrivada.sign(b"message",ec.ECDSA(hashes.SHA256()))
  T2 = time.time()

  sign_prom_list.append( T2 - T1 )

  try:
    #Al igual que la de verificacion
    T1 = time.time()
    llavePublica.verify(firma,b"message",ec.ECDSA(hashes.SHA256()))
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except InvalidSignature:
    print("BAD SIGNATURE")

# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(sign_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
sign_prom_list = [i for i in sign_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
sign_prom_list = [i for i in sign_prom_list if i > (q25 - 1.5*IQR)]

sign_values["ECDSA BF"] = np.mean(sign_prom_list)
sign_prom_list.clear()


# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(verify_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
verify_prom_list = [i for i in verify_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
verify_prom_list = [i for i in verify_prom_list if i > (q25 - 1.5*IQR)]

verify_values["ECDSA BF"] = np.mean(verify_prom_list)
verify_prom_list.clear()