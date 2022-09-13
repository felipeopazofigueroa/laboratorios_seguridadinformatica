import rot
import vigenere
import hashlib

#LAB 2 Seguridad Informatica - Oliver Lillo / Felipe Opazo

mensaje = input("Ingrese un mensaje a codificar: ")
hasheado = hashlib.sha256(mensaje.encode())

with open("mensajedeentrada.txt","w") as entrada:
    entrada.write(mensaje)

encriptado = rot.main(mensaje,18)
encriptado = vigenere.main(encriptado,"encriptar","randompasswd")

with open("mensajeseguro.txt","w") as cipher:
    cipher.write(encriptado)
    cipher.write(";"+hasheado.hexdigest())





