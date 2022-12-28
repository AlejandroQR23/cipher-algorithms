import time
import numpy as np
from Crypto.Hash import SHA384
from structures import hash_prom_list,average,iter

for i in range(iter):
  cadenaHash = b"MiCadenaHashSha2"
    
  # Creacion de objetos hash sha-2 y su codificacion
  hash_sha2_384 = SHA384.new( cadenaHash )
  T1 = time.time()
  hash_sha2_384.update( b"update")  # SHA384
  T2 = time.time()

  average = average+(T2-T1)

print(average/iter)
hash_prom_list.append(average/iter)