from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import time
import numpy as np
from structures import encryp_prom_list,decryp_prom_list,encryp_values,decryp_values,average

for i in range(150):
  cha_plaintext = b'Texto prueba para el primer proyecto de criptografia'
  cha_key = get_random_bytes(32)
  cha_cipher = ChaCha20.new(key=cha_key)
  T1 = time.time()
  cha_ciphertext = cha_cipher.encrypt(cha_plaintext)
  T2 = time.time()

  average = average+(T2-T1)

  nonce = cha_cipher.nonce

  try:
    cha_cipher = ChaCha20.new(key=cha_key, nonce=nonce)
    T1 = time.time()
    cha_plaintext_bits = cha_cipher.decrypt(cha_ciphertext)
    T2 = time.time()
  except (ValueError, KeyError):
    print("Incorrect decryption")

  decryp_prom_list.append(T2 - T1)

print(average)
encryp_prom_list.append(T2 - T1)