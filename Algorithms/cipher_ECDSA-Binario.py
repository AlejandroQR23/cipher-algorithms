import time
import numpy as np
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from structures import sign_prom_list,verify_prom_list,VerifyAverage,signatureAverage,iter

for i in range(iter):
  llaveFirmaPrivada = ec.generate_private_key(ec.SECT571K1())
  llavePublica = llaveFirmaPrivada.public_key()

  T1 = time.time()
  firma = llaveFirmaPrivada.sign(b"message",ec.ECDSA(hashes.SHA256()))
  T2 = time.time()

  signatureAverage = signatureAverage+(T2-T1)

  try:
    #Al igual que la de verificacion
    T1 = time.time()
    llavePublica.verify(firma,b"message",ec.ECDSA(hashes.SHA256()))
    T2 = time.time()
    
    VerifyAverage = VerifyAverage+(T2-T1)

  except InvalidSignature:
    print("BAD SIGNATURE")

print(signatureAverage/iter)
sign_prom_list.append(signatureAverage/iter)

print(VerifyAverage/iter)
verify_prom_list.append(VerifyAverage/iter)