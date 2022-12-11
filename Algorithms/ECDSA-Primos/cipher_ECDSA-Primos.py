for i in range(iter):
  #Usamos la curva de 521 bits
  llaveFirmaPrivada = SigningKey.generate(curve=NIST521p)
  llavePublica = llaveFirmaPrivada.verifying_key

  #Creamos la firma
  T1 = time.time()
  firma = llaveFirmaPrivada.sign(b"message")
  T2 = time.time()

  sign_prom_list.append( T2 - T1 )

  try:
    #Al igual que la de verificacion
    T1 = time.time()
    llavePublica.verify(firma, b"message")
    T2 = time.time()
    verify_prom_list.append( T2 - T1 )
  except BadSignatureError:
    print("BAD SIGNATURE")

# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(sign_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
sign_prom_list = [i for i in sign_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
sign_prom_list = [i for i in sign_prom_list if i > (q25 - 1.5*IQR)]

sign_values["ECDSA PF"] = np.mean(sign_prom_list)
sign_prom_list.clear()


# Calculo y eliminacion de valores atipicos para la verificacion.
q75,q25 = np.percentile(verify_prom_list,[75,25])
IQR = q75 - q25

# Elimina los valores por encima del limite superior
verify_prom_list = [i for i in verify_prom_list if i < (q75 + 1.5*IQR)]
# Elimina los valores por debajo del limite inferior
verify_prom_list = [i for i in verify_prom_list if i > (q25 - 1.5*IQR)]

verify_values["ECDSA PF"] = np.mean(verify_prom_list)
verify_prom_list.clear()