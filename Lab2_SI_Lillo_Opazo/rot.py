def rot13(message,number):
    Rot13=''
    alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if i in alphabit:
            Rot13 += alphabit[alphabit.index(i) + number]
        else:
            Rot13 += i
    return Rot13

def main(mensaje,numero):
    if(numero < 0):
        numero = 26 + numero
    cifrado = rot13(mensaje, numero)
    return(cifrado)
