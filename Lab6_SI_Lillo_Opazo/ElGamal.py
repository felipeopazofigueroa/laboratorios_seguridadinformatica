import random
from math import pow

a = random.randint(2, 10)

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b;
	else:
		return gcd(b, a % b)

# Generating large random numbers
def gen_key(q):

	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

# Modular exponentiation
def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c


def encrypt(msg, q, h, g):

	en_msg = []

	k = gen_key(q)# Private key for sender
	s = power(h, k, q)
	p = power(g, k, q)
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])

	print("g^k usado : ", p)
	print("g^ak usado : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

def decrypt(en_msg, p, key, q): 
    dr_msg = []
    h = power(int(p), int(key), int(q))
    for i in range(0, len(en_msg)):        
        if( (en_msg[i] == ",") or (en_msg[i] == " ") ):
            pass
        else:            
            dr_msg.append(chr(int(int(en_msg[i])/h)))

    
    dmsg = ''.join(dr_msg)    
    return dmsg

def q():
    q = random.randint(pow(10, 20), pow(10, 50))
    return q

def g(q):
    g = random.randint(2, q)
    return g

def h(g,key,q):
    h = power(g, key, q)
    return h


