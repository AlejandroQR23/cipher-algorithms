import time
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from structures import sign_prom_list,verify_prom_list,sign_values,verify_values,signatureAverage,VerifyAverage,iter

for i in range(iter):
  message = b'To be signed'
  keys = RSA.generate(2048)
  private_key = keys.export_key()
  public_key = keys.publickey()
  h = SHA256.new(message)
  T1 = time.time()
  signature = pss.new(keys).sign(h)
  T2 = time.time()

  signatureAverage = signatureAverage+(T2-T1)

  verifier = pss.new(keys)
  try:
    T1 = time.time()
    verifier.verify(h, signature)
    T2 = time.time()

    VerifyAverage = VerifyAverage+(T2-T1)
    
  except (ValueError, TypeError):
    print ("The signature is not authentic.")

print(signatureAverage/iter)
sign_prom_list.append(signatureAverage/iter)

print(VerifyAverage/iter)
verify_prom_list.append(VerifyAverage/iter)