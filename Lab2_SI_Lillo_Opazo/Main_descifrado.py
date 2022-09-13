import rot
import vigenere
import hashlib

archivo = open("mensajeseguro.txt","r")
todasLasLineas = archivo.readlines()
for i in range(0,len(todasLasLineas)):
    split_Txt = todasLasLineas[i].split(";")
archivo.close()

descifrado = vigenere.main(split_Txt[0],"descifrar","randompasswd")
descifrado = rot.main(descifrado,-18)

print("El mensaje original es:",descifrado)
desc = hashlib.sha256(descifrado.encode())

with open("mensajeseguro.txt","r") as lectura:
    print(desc.hexdigest())
    print(split_Txt[1])
    if(desc.hexdigest() != split_Txt[1]):
        print("El mensaje original fue modificado!!")
    else:
        print("El mensaje es autentico")