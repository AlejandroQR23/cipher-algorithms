import time
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from structures import sign_prom_list,verify_prom_list,sign_values,verify_values,average

for i in range(150):
  message = b'To be signed'
  keys = RSA.generate(2048)
  private_key = keys.export_key()
  public_key = keys.publickey()

  h = SHA256.new(message)

  T1 = time.time()
  signature = pss.new(keys).sign(h)
  T2 = time.time()

  average = average+(T2-T1)

  verifier = pss.new(keys)
  try:
    T1 = time.time()
    verifier.verify(h, signature)
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except (ValueError, TypeError):
    print ("The signature is not authentic.")

print(average)
sign_prom_list.append(average)