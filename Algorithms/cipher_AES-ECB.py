from Crypto.Random import get_random_bytes
import time
import numpy as np
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values,averageDecript,averageEncript,iter

for i in range(iter):
  data = b'secret'
  key = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)
  padded_block = pad(data, AES.block_size)
  T1 = time.time()
  ct_bytes = cipher.encrypt(padded_block)
  T2 = time.time()
  
  averageEncript = averageEncript+(T2-T1)

  try:
    T1 = time.time()
    cipher = AES.new(key, AES.MODE_ECB)
    T2 = time.time()
    
    averageDecript = averageDecript+(T2-T1)

  except (ValueError, KeyError):
    print("Incorrect decryption")

print(averageEncript/iter)
encryp_prom_list.append(averageEncript/iter)

print(averageDecript/iter)
decryp_prom_list.append(averageDecript/iter)