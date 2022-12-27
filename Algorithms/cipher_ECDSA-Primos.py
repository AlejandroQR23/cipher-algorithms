import time
import numpy as np
from ecdsa import SigningKey, NIST521p, BadSignatureError
from structures import sign_prom_list,verify_prom_list,sign_values,verify_values,average

for i in range(150):
  #Usamos la curva de 521 bits
  llaveFirmaPrivada = SigningKey.generate(curve=NIST521p)
  llavePublica = llaveFirmaPrivada.verifying_key

  #Creamos la firma
  T1 = time.time()
  firma = llaveFirmaPrivada.sign(b"message")
  T2 = time.time()

  average = average+(T2-T1)

  try:
    #Al igual que la de verificacion
    T1 = time.time()
    llavePublica.verify(firma, b"message")
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except BadSignatureError:
    print("BAD SIGNATURE")

print(average)
sign_prom_list.append(average)