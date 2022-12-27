from Crypto.Random import get_random_bytes
import time
import numpy as np
from Crypto.Cipher import AES
from structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values,average

for i in range(150):
  header = b"header"
  data = b"secret"
  aes_gcm_key = get_random_bytes(16)
  aes_gcm_cipher = AES.new(aes_gcm_key, AES.MODE_GCM)
  aes_gcm_cipher.update(header)
  T1 = time.time()
  aes_gcm_ciphertext, tag = aes_gcm_cipher.encrypt_and_digest(data)
  T2 = time.time()

  average = (T2-T1)+average

  nonce = aes_gcm_cipher.nonce

  try:
      aes_gcm_cipher = AES.new(aes_gcm_key, AES.MODE_GCM, nonce)
      aes_gcm_cipher.update(header)
      T1 = time.time()
      plaintext = aes_gcm_cipher.decrypt_and_verify(aes_gcm_ciphertext, tag)
      T2 = time.time()
      decryp_prom_list.append(T2 - T1)
  except (ValueError, KeyError):
      print("Incorrect decryption")

print(average)
encryp_prom_list.append(T2 - T1)