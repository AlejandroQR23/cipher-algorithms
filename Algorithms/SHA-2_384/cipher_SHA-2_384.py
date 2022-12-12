import time
import numpy as np
from Crypto.Hash import SHA384


for i in range(iter):
  cadenaHash = b"MiCadenaHashSha2"
    
  # Creacion de objetos hash sha-2 y su codificacion
  hash_sha2_384 = SHA384.new( cadenaHash )
  T1 = time.time()
  hash_sha2_384.update( b"update")  # SHA384
  T2 = time.time()

  hash_prom_list.append(T2 - T1)
  
# Calculo y eliminacion de valores atipicos para el hash.
q75,q25 = np.percentile(hash_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
hash_prom_list = [i for i in hash_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
hash_prom_list = [i for i in hash_prom_list if i > (q25 - 1.5*IQR)]

hash_values["SHA2-384"] = np.mean(hash_prom_list)
hash_prom_list.clear()