#LAB 5 SEGURIDAD INFORMATICA - Oliver Lillo Castro / Felipe Opazo Figueroa

import socket
from diffie_hellman import *
import cifrados
from cifrados import *

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("", 8050))

#Parámetro indica las conexiones simultaneas que se pueden tener
servidor.listen(1)
cliente, addr = servidor.accept()

cont = 0
validador = False

while True:
    #Recibe el numero (P) desde el cliente
    if(validador == False):
        mensaje_Cliente = cliente.recv(1024)
        print("Numero P: ", mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))
        temp_P = int(mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))
        cont+=1
        validador = True
    
    else:
        if(cont == 1):
            #Recibe el numero (G) desde el cliente
            mensaje_Cliente = cliente.recv(1024)
            print("Numero G: ", mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))
            temp_G = int(mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))

            #Calcula la llave publica (B) por Diffie Hellman que le va a enviar al Cliente a partir de los valores entregados de P y G
            mensaje_Servidor = calcular(temp_G,temp_P)
            cliente.send(str(mensaje_Servidor).encode(encoding = "ascii", errors = "ignore"))
            cont+=1

        elif(cont==2):
            #Recibe la llave publica (A) desde el Cliente 
            mensaje_Cliente = cliente.recv(1024)
            llaveA = int(mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))
            print("Llave publica Cliente (A): ", mensaje_Cliente.decode(encoding = "ascii", errors = "ignore"))
            cont+=1
        else:
            #Diffie Hellman para calcular la llave privada para establecer comunicacion usando los valores de (A), (b) y (P)
            privateKey_Comunicacion = obtener_publico(llaveA,lista_numerosPrivados[0],temp_P)
            cliente.send(str(privateKey_Comunicacion).encode(encoding = "ascii", errors = "ignore"))

            #Se muestra la llave privada para establecer comunicacion entre ambas entidades (Cliente/Servidor)
            llaveComunicacionPrivada = cliente.recv(1024)
            print("\n == Llave privada para realizar comunicacion: ", llaveComunicacionPrivada.decode(encoding = "ascii", errors = "ignore")," ==")

            mensaje_Cliente = cliente.recv(1024)
            seleccionCifrado_Cliente = mensaje_Cliente.decode(encoding = "ascii", errors = "ignore")

            #Abre archivo de mensaje para verificar el mensaje cifrado enviado desde el cliente
            archivo = open("mensajedeentrada.txt","rb")
            todasLasLineas = archivo.readlines()

            archivo_Nonce = open("nonce.txt","rb")
            LineasNonce = archivo_Nonce.readlines()

            #Si el cifrado usado es DES, entonces
            if(int(seleccionCifrado_Cliente)== 1):

                #Se usa la llave privada obtenida de diffie hellman para trabajar con 8 Bytes
                key = privateKey_Comunicacion.to_bytes(8,"big")

                print("Mensaje recibido (cifrado DES): ",str(todasLasLineas[0]))

                #Se llama a la funcion de descifrado de DES para obtener el mensaje original enviado desde el cliente
                descifrado = str(cifrados.descifrar_DES(todasLasLineas[0],key,LineasNonce[0]))
                
                #Se manda el mensaje original descifrado a un txt
                with open("mensajeseguro.txt","w+") as entrada:
                    entrada.write(descifrado)
                
                archivo = open("mensajeseguro.txt","r")
                todasLasLineas = archivo.readlines()
                
                print("\nMensaje recibido descifrado: ", todasLasLineas[0])

                archivo.close()
                archivo_Nonce.close()
                break
            
            #Si el cifrado usado es AES, entonces
            elif(int(seleccionCifrado_Cliente) == 2):

                #Se usa la llave privada obtenida de diffie hellman para trabajar con 16 Bytes
                key = privateKey_Comunicacion.to_bytes(16,"big")

                print("Mensaje recibido (cifrado AES): ",str(todasLasLineas[0]))

                #Se llama a la funcion de descifrado de AES para obtener el mensaje original enviado desde el cliente
                descifrado = str(cifrados.descifrar_AES(todasLasLineas[0],key,LineasNonce[0]))
                
                #Se manda el mensaje original descifrado a un txt
                with open("mensajeseguro.txt","w+") as entrada:
                    entrada.write(descifrado)
                
                archivo = open("mensajeseguro.txt","r")
                todasLasLineas = archivo.readlines()
                
                print("\nMensaje recibido descifrado: ", todasLasLineas[0])

                archivo.close()
                archivo_Nonce.close()
                break

            #Si el cifrado usado es 3DES, entonces
            elif(int(seleccionCifrado_Cliente) == 3):

                #Se usa la llave privada obtenida de diffie hellman para trabajar con 24 Bytes
                key = privateKey_Comunicacion.to_bytes(24,"big")
            
                print("Mensaje recibido (cifrado por 3DES): ",str(todasLasLineas[0]))

                #Se llama a la funcion de descifrado de 3DES para obtener el mensaje original enviado desde el cliente
                descifrado = str(cifrados.descifrar_3DES(todasLasLineas[0],key,LineasNonce[0]))
                
                #Se manda el mensaje original descifrado a un txt
                with open("mensajeseguro.txt","w+") as entrada:
                    entrada.write(descifrado)
                
                archivo = open("mensajeseguro.txt","r")
                todasLasLineas = archivo.readlines()
                
                print("\nMensaje recibido descifrado: ", todasLasLineas[0])

                archivo.close()
                archivo_Nonce.close()
                break

cliente.close()
servidor.close()

print("== Conexiones cerradas ==")