lista_numerosPrivados = []

#Algoritmo de Diffie Hellman
def obtener_publico(base, exponente, modulo):    
    numeroPublico = (base**exponente) % modulo
    return numeroPublico


#Funcion para validar si es primo
def es_primo(p):
    if(p < 1):
        print("No es primo")
        return True
    elif(p == 2):
        return False
    else:
        for n in range(2, p):
            if p % n == 0:
                print("No es primo", n, "es divisor")
                return True
        return False

def calcular(g,p):
    numero_privado = 0
    while( (numero_privado < 1) or (numero_privado >= p-1) ):
        #Se ingresa el numero privado requerido para calcular diffie hellman
        numero_privado = int(input("Introduzca su número privado(0 < a,b < p-1): ")) 

        #Ingresa numeros privados a una lista para poder ser acceder a ellos desde otra funcion
        global lista_numerosPrivados
        lista_numerosPrivados.append(numero_privado)  

    numero = obtener_publico(g,numero_privado,p)
    return numero

def p():       
    validar = True
    while(validar):
        #Ingresa y valida si el numero es primo
        p = int(input("Introduzca un número primo p: "))
        validar = es_primo(p)
    return (p)

def g(p):
    g = 0
    while( (g < 1) or (g >= p) ):
        g = int(input("Introduzca un número g, tal que (0 < g < p): "))
    return(g)
