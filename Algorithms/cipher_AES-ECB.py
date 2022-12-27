from Crypto.Random import get_random_bytes
import time
import numpy as np
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values,average

for i in range(150):
  data = b'secret'
  key = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)
  padded_block = pad(data, AES.block_size)
  T1 = time.time()
  ct_bytes = cipher.encrypt(padded_block)
  T2 = time.time()
  
  average = average+(T2-T1)

  try:
    T1 = time.time()
    cipher = AES.new(key, AES.MODE_ECB)
    T2 = time.time()
    decryp_prom_list.append(T2 - T1)
  except (ValueError, KeyError):
    print("Incorrect decryption")

print(average)
encryp_prom_list.append(average)