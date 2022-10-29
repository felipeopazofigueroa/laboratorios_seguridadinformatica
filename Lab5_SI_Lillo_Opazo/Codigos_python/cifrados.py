from Cryptodome.Cipher import DES, DES3, AES

def cifrar_DES(mensaje,llave):
    cipher = DES.new(llave, DES.MODE_EAX)

    #Nonce guarda valores aleatorios de bytes para asegurar autenticidad en descifrado del mensaje
    nonce = cipher.nonce

    #Se declara ciphertext para guardar el mensaje cifrado usando ASCII
    ciphertext = cipher.encrypt_and_digest(mensaje.encode('ascii'))

    with open("mensajedeentrada.txt","wb") as entrada:

        #Se escribe el texto cifrado (en bytes) en el archivo
        entrada.write(ciphertext[0])

    with open("nonce.txt","wb") as txt_Nonce:
        #Se ingresa el nonce declarado anteriormente en otro txt (tambien se escribe en bytes)
        txt_Nonce.write(nonce)
    

    return ciphertext

def descifrar_DES(textoCifrado, llave, nonce):
    cipher = DES.new(llave, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(textoCifrado)
    return plaintext.decode("ascii")

'''======================================'''

def cifrar_AES(mensaje,llave):
    cipher = AES.new(llave, AES.MODE_EAX)

    #Nonce guarda valores aleatorios de bytes para asegurar autenticidad en descifrado del mensaje
    nonce = cipher.nonce

    ciphertext = cipher.encrypt_and_digest(mensaje.encode('ascii'))

    with open("mensajedeentrada.txt","wb") as entrada:

        #Se escribe el texto cifrado (en bytes) en el archivo
        entrada.write(ciphertext[0])

    with open("nonce.txt","wb") as txt_Nonce:
        #Se ingresa el nonce declarado anteriormente en otro txt (tambien se escribe en bytes)
        txt_Nonce.write(nonce)

    return ciphertext

def descifrar_AES(textoCifrado,llave,nonce):
    cipher = AES.new(llave, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(textoCifrado)
    return plaintext.decode('ascii')


'''======================================'''

def cifrar_3DES(mensaje,llave):
    #Revisar el largo de la llave para que no degenere a llave de DES y poder utilizar 3DES
    if llave[:8] == llave[8:16] and llave[-8:] == llave[8:16]:
        cipher = DES.new(llave[:8], DES.MODE_EAX)
    elif llave[:8] == llave[8:16]:
        cipher = DES3.new(llave[8:], DES3.MODE_EAX)
    elif llave[-8:] == llave[8:16]:
        cipher = DES3.new(llave[:-8], DES3.MODE_EAX)
    else:
        cipher = DES3.new(llave, DES3.MODE_EAX)

    #Nonce guarda valores aleatorios de bytes para asegurar autenticidad en descifrado del mensaje
    nonce = cipher.nonce
    ciphertext = cipher.encrypt_and_digest(mensaje.encode('ascii'))

    with open("mensajedeentrada.txt","wb") as entrada:

        #Se escribe el texto cifrado (en bytes) en el archivo
        entrada.write(ciphertext[0])

    with open("nonce.txt","wb") as txt_Nonce:
        #Se ingresa el nonce declarado anteriormente en otro txt (tambien se escribe en bytes)
        txt_Nonce.write(nonce)

    
    return ciphertext

def descifrar_3DES(textoCifrado, llave, nonce):
    #Revisar el largo de la llave para que no degenere a llave de DES y poder utilizar 3DES
    if llave[:8] == llave[8:16] and llave[-8:] == llave[8:16]:
        cipher = DES.new(llave[:8], DES.MODE_EAX, nonce=nonce)
    elif llave[:8] == llave[8:16]:
        cipher = DES3.new(llave[8:], DES3.MODE_EAX, nonce=nonce)
    elif llave[-8:] == llave[8:16]:
        cipher = DES3.new(llave[:-8], DES3.MODE_EAX, nonce=nonce)
    else:
        cipher = DES3.new(llave, DES3.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt(textoCifrado)
    return plaintext.decode('ascii')