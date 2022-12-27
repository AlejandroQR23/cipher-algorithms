import time
import numpy as np
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values,average

for i in range(150):
  message = b'You can attack now!'
  keys = RSA.generate(2048)
  public_key = keys.publickey()

  cipher = PKCS1_OAEP.new(public_key)
  T1 = time.time()
  ciphertext = cipher.encrypt(message)
  T2 = time.time()

  average = average+(T2-T1)

  try:
    cipher = PKCS1_OAEP.new(keys)
    T1 = time.time()
    message = cipher.decrypt(ciphertext)
    T2 = time.time()
    decryp_prom_list.append(T2 - T1)
  except(ValueError, TypeError):
    print("Incorrect decryption")

print(average)
encryp_prom_list.append(average)