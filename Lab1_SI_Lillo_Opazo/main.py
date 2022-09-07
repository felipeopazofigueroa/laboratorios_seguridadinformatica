import peticiones
import rot
import vigenere

#LAB 1 Seguridad Informatica - Oliver Lillo / Felipe Opazo

def desafio1():
    while(True):
        mensaje = input("Ingrese un mensaje a codificar: ")

        if not mensaje.isalpha():
            print("Ingrese solo letras desde A hasta Z")
            continue

        else:
            break

    encriptado = rot.main(mensaje,8)
    print("El rot 8 es: "+encriptado)

    encriptado = vigenere.main(encriptado,"encriptar","heropassword")
    print("El vigenere es: "+encriptado)

    encriptado = rot.main(encriptado,12)
    print("El rot 12 es: "+encriptado)

    peticiones.curlPost(encriptado)



print("desafio 1")
desafio1()

print("\n====================\n")

print("desafio 2")
def desafio2():
    msg = peticiones.curlGet()
    mensaje = msg.split('"')
    print(msg)
    descifrado = rot.main(mensaje[3],-12)
    print("El rot -12 es: "+descifrado)

    descifrado = vigenere.main(descifrado,"descifrar","finispasswd")
    print("El vigenere es: "+descifrado)

    descifrado = rot.main(descifrado,-8)
    print("El rot -8 es: "+descifrado)


desafio2()
