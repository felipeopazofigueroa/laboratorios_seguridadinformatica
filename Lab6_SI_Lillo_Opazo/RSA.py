def es_primo(p):
    
    if(p < 1):
        print("no es primo")
        return True
    elif(p == 2):
        print("Es primo")
        return False
    else:
        for n in range(2, p):
            if p % n == 0:
                print("No es primo", n, "es divisor")
                return True
        print("Es primo")
        return False

def pORq():       
    validar = True
    while(validar):
        p = int(input("Introduzca el número primo 'p': "))
        validar = es_primo(p)
    return (p)
	
def calculae(phi):
	e=2
	le=[]
	while e>1 and e<phi :
		if mcd(e,phi)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	print("VALORES PARA (e)= "+str(le))
	e=int(input("Valor de (e)= "))
	while mcd(e,phi)!=1:
		print("Eliga un valor de la lista !!!")
		e=int(input("Valor de (e)= "))
	return e

def mcd(e,phi):
	m=phi%e
	while m!=0:
		phi=e
		e=m
		m=phi%e
	return e

def congruente(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')

def cifrarmensaje(msj,e,n):
    e = e
    n = n       
    x=""
    m=0
    for i in msj:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x += str(c)
            x += " "
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x += str(c)
            x += " "
        elif(i.isspace()):
            spc=400
            x += str(400)
            x += " "
    return x[:-1]



def descifrarmensaje(msj,d, n):
    d = d
    n = n
    txt=msj.split(' ')
    x=''
    m=0
    for i in txt:
        if(i=="400"):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
