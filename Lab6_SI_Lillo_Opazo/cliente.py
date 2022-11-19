import socket
import RSA
import funcionesTxt
import ElGamal

host = "LocalHost"
port = 5656

objSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objSocket.connect((host,port))
print("cliente iniciado")



while True:
    print("1. RSA\n2. El Gamal\notro. Salir")
    opcion = input("ingrese número de la opcion: ")
    objSocket.send(str(opcion).encode(encoding = "ascii", errors = "ignore"))
    
    if(opcion == "1"):
        p = RSA.pORq()
        objSocket.send(str(p).encode(encoding = "ascii", errors = "ignore"))
        
        q = (objSocket.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Servidor: ", q)

        n = int(p)*int(q)
        ø = (int(p)-1)*(int(q)-1)
        print("n = "+str(n)+"\nø = "+str(ø))
        e = RSA.calculae(int(ø))
        objSocket.send(str(e).encode(encoding = "ascii", errors = "ignore"))    

        key_public=[n,e]

        print("Servidor: ", (objSocket.recv(1024)).decode(encoding = "ascii", errors = "ignore"))

        mensaje=input("Ingrese Mensaje a enviar: ")
        mensaje_cifrado = RSA.cifrarmensaje(mensaje,e,n)
        print("Mensaje Cifrado : "+str(mensaje_cifrado))
        objSocket.send(str(mensaje_cifrado).encode(encoding = "ascii", errors = "ignore"))

        funcionesTxt.escribir(mensaje_cifrado,"mensajeentradaRSA.txt")


    elif(opcion == "2"):
        q = ElGamal.q()
        objSocket.send(str(q).encode(encoding = "ascii", errors = "ignore"))

        g = (objSocket.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Servidor: ", str(g))

        key = ElGamal.gen_key(int(q))# Private key for receiver
        h = ElGamal.h(int(g),key,int(q))
        print("g usado : ",str(g))
        print("g^a usado : ",str(h))

        msj = input("ingresar mensaje a encriptar: ")
        mensaje_cifrado, p = ElGamal.encrypt(msj, int(q), int(h), int(g))

        objSocket.send(str(mensaje_cifrado).encode(encoding = "ascii", errors = "ignore"))

        mensaje = str(mensaje_cifrado)+";"+str(p)+(";")+str(key)
        
        funcionesTxt.escribir(mensaje,"mensajeentradaElGamal.txt")


    else:        
        print("conexión cerrada")
        break

objSocket.close()

