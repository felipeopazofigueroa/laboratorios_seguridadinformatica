
def leer(nombre):  
        baseDeDatos=open(nombre,"r")
        registros=baseDeDatos.readlines()
        baseDeDatos.close()
        return registros

def escribir(mensaje,nombre):
        baseDeDatos=open(nombre,"w+")
        baseDeDatos.writelines(mensaje)
        baseDeDatos.close()
        
  
        

   
        
    
        
