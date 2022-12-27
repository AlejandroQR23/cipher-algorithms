import time
import numpy as np
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from structures import sign_prom_list,verify_prom_list,sign_values,verify_values,average

for i in range(150):
  llaveFirmaPrivada = ec.generate_private_key(ec.SECT571K1())
  llavePublica = llaveFirmaPrivada.public_key()

  T1 = time.time()
  firma = llaveFirmaPrivada.sign(b"message",ec.ECDSA(hashes.SHA256()))
  T2 = time.time()

  average = average+(T2-T1)

  try:
    #Al igual que la de verificacion
    T1 = time.time()
    llavePublica.verify(firma,b"message",ec.ECDSA(hashes.SHA256()))
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except InvalidSignature:
    print("BAD SIGNATURE")

print(average)
sign_prom_list.append( T2 - T1 )