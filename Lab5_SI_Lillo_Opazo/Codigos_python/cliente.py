#LAB 5 SEGURIDAD INFORMATICA - Oliver Lillo Castro / Felipe Opazo Figueroa

import socket
from diffie_hellman import *
import cifrados

host = "LocalHost" #Se define un host de forma local
port = 8050

objetoSocket = socket.socket()
 
#Conexion al servidor
objetoSocket.connect((host, port))

while True:
    #Se llama a la funcion p() para generar un numero (P) para enviar al servidor
    llavePublica_Cliente = str(p())
    objetoSocket.send(llavePublica_Cliente.encode(encoding = "ascii", errors = "ignore"))
    temp_P = int(llavePublica_Cliente.encode(encoding = "ascii", errors = "ignore"))

    #Se llama a la funcion g() tomando el valor de (P) como argumento y se envia al servidor
    llavePublica_Cliente_G = str(g(int(llavePublica_Cliente)))
    objetoSocket.send(llavePublica_Cliente_G.encode(encoding = "ascii", errors = "ignore"))
    temp_G = int(llavePublica_Cliente_G.encode(encoding = "ascii", errors = "ignore"))

    #Se recibe llave publica (B) desde el servidor
    mensaje_Servidor = objetoSocket.recv(1024)
    llaveB = int(mensaje_Servidor.decode(encoding = "ascii", errors = "ignore"))
    print("Llave Publica Servidor (B): ", mensaje_Servidor.decode(encoding = "ascii", errors = "ignore"))

    #Se calcula llave publica (A) para enviar al servidor
    llavePublica_Cliente_A = calcular(temp_G,temp_P)
    objetoSocket.send(str(llavePublica_Cliente_A).encode(encoding = "ascii", errors = "ignore"))
    
    #Se recibe la llave privada para establecer comunicacion
    llaveComunicacionPrivada = objetoSocket.recv(1024)
    print("\n == Llave privada para realizar comunicacion: ", llaveComunicacionPrivada.decode(encoding = "ascii", errors = "ignore")," ==")

    privateKey_Comunicacion = obtener_publico(llaveB,lista_numerosPrivados[0],temp_P)
    objetoSocket.send(str(privateKey_Comunicacion).encode(encoding = "ascii", errors = "ignore"))

    menu_seleccion_cifrado = int(input("Cifrado a utilizar para cifrar mensaje\n1. DES\n2. AES\n3. 3DES\n => "))
    
    if (menu_seleccion_cifrado == 1):
        #Se toma la llave privada obtenida de diffie hellman usando 8 Bytes 
        key = privateKey_Comunicacion.to_bytes(8,"big")
        mensajeFinal = input("Ingrese el mensaje que desea cifrar: ")
        
        #Se llama a la funcion de cifrado DES para poder ingresar el cifrado en un txt
        cifrados.cifrar_DES(mensajeFinal,key)
        print("\nMensaje Cifrado por DES enviado")

        #Se avisa al servidor del envio del mensaje cifrado 
        objetoSocket.send(str(menu_seleccion_cifrado).encode(encoding = "ascii", errors = "ignore"))
        break

    elif (menu_seleccion_cifrado == 2):
        #Se toma la llave privada obtenida de diffie hellman usando 16 bytes
        key = privateKey_Comunicacion.to_bytes(16,"big")
        mensajeFinal = input("Ingrese el mensaje que desea cifrar: ")

        #Se llama a la funcion de cifrado AES para poder ingresar el cifrado en un txt
        cifrados.cifrar_AES(mensajeFinal,key)
        print("\nMensaje Cifrado por AES enviado")

        #Se avisa al servidor del envio del mensaje cifrado 
        objetoSocket.send(str(menu_seleccion_cifrado).encode(encoding = "ascii", errors = "ignore"))

        break

    elif (menu_seleccion_cifrado == 3):
        #Se toma la llave privada obtenida de diffie hellman usando 24 Bytes
        key = privateKey_Comunicacion.to_bytes(24,"big")
        mensajeFinal = input("Ingrese el mensaje que desea cifrar: ")

        #Se llama a la funcion de cifrado 3DES para poder ingresar el cifrado en un txt
        cifrados.cifrar_3DES(mensajeFinal,key)
        print("\nMensaje Cifrado por 3DES enviado")

        objetoSocket.send(str(menu_seleccion_cifrado).encode(encoding = "ascii", errors = "ignore"))
        break

objetoSocket.close()
print("\n == Conexión cerrada ==")