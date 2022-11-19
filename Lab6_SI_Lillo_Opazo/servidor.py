import socket
import RSA
import funcionesTxt
import ElGamal

host = "LocalHost"
port = 5656


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Servidor en espera de conexiones")
active, addr = server.accept()

while True:
    opcion = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
    
    if(str(opcion) == "1"):
        p = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Cliente: ", p)
        
        q = RSA.pORq()
        active.send(str(q).encode(encoding = "ascii", errors = "ignore"))

        n = int(p)*int(q)
        phi = (int(p)-1)*(int(q)-1)
        print("n = "+str(n)+"\nø = "+str(phi))
        
        e = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Cliente: ", e)
        key_public = ("LLAVE PUBLICA = "+str([n,int(e)]))
        active.send(str(key_public).encode(encoding = "ascii", errors = "ignore"))
        print(key_public)
        
        d = RSA.congruente(int(e),phi)
        key_private=[n,d]
        print("LLAVE PRIVADA = "+str(key_private))

        mensaje_cifrado = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Cliente: ", mensaje_cifrado)

        mensaje_cifrado = funcionesTxt.leer("mensajeentradaRSA.txt")
        print(mensaje_cifrado)

        mensaje_descifrado = RSA.descifrarmensaje(str(mensaje_cifrado)[2 : -2],d,n)    
        print("Mensaje Descifrado : "+str(mensaje_descifrado))

        funcionesTxt.escribir(mensaje_descifrado,"mensajerecibidoRSA.txt")

        
    elif(str(opcion) == "2"):
        q = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Cliente: ", str(q))
        
        g = ElGamal.g(int(q))
        print("g: ", str(g)) 
        active.send(str(g).encode(encoding = "ascii", errors = "ignore"))       
        
       

        mensaje_cifrado = (active.recv(1024)).decode(encoding = "ascii", errors = "ignore")
        print("Cliente: ", mensaje_cifrado)       

        mensaje_cifrado = funcionesTxt.leer("mensajeentradaElGamal.txt")

        mensaje = str(mensaje_cifrado).split(";")
        
        x = str(mensaje[0])[3 : -1]
        key = mensaje[2][:-2]
        y = x.split(", ")
        
        mensaje_descifrado = ElGamal.decrypt(y,int(mensaje[1]),int(key),int(q))
        print("Mensaje Descifrado : "+str(mensaje_descifrado))


        funcionesTxt.escribir(mensaje_descifrado,"mensajerecibidoElGamal.txt")


    else:        
        print("conexión cerrada")
        break

active.close()

