#Converciones.py
"""
Programa que mediante un men� permite realizar converciones entre diferentes unidades
de medida, debe trabajar con por lo menos 4 unidades de medida longitudinal y las
conversiones se deben realizar entre ellas.
"""
list=["Centrimetro","Metro","Decametro","Hectometro","Kilometro"]   #Creamos una lista
x=" "
z=" "
y=0.0
print ("Las opciones son:") 
for x in list:
    print (x)
x=input("Indique la medida inicial: ")
while x!="Centimetro" and x!="Metro" and x!="Decametro" and x!="Hectometro" and x!="Kilometro":
    x=input("Indique una medida de la lista: ") #Usamos while para poder comprobar que solo tome valores de la lista
y=int(input("Ingrese el valor de la medida: "))    
while y<0:
    y=input("Ingrese un valor positivo: ")        #Ingresamos un valor que deseamos convertir
z=input("Ingrese a que medida desea convertirlo, seleccione una de la lista dada: ")
while z!="Centimetro" and z!="Metro" and z!="Decametro" and z!="Hectometro" and z!="Kilometro":
    z=input("Ingrese una medida de la lista dada: ")
if x=="Centimetro" and z=="Metro":
    print ("El resultado es: ",y/100.0)
elif x=="Centimetro" and z=="Decametro":
    print ("El resultado es: ",y/1000.0)
elif x=="Centimetro" and z=="Hectometro":
    print ("El resultado es: ",y/10000.0)
elif x=="Centimetro" and z=="Kilometro":
    print ("El resultado es: ",y/100000.0)
elif x=="Metro" and z=="Centimetro":
    print ("El resultado es: ",y*100.0)
elif x=="Metro" and z=="Decametro":
    print ("El resultado es: ",y/10.0)
elif x=="Metro" and z=="Hectometro":
    print ("El resultado es: ",y/100.0)
elif x=="Metro" and z=="Kilometro":
    print ("El resultado es: ",y/1000.0)
elif x=="Decametro" and z=="Centimetro":
    print ("El resultado es: ",y*1000.0)
elif x=="Decametro" and z=="Metro":
    print ("El resultado es: ",y*10.0)
elif x=="Decametro" and z=="Hectometro":
    print ("El resultado es: ",y/10.0)
elif x=="Decametro" and z=="Kilometro":
    print ("El resultado es: ",y/100.0)
elif x=="Hectometro" and z=="Centimetro":
    print ("El resultado es: ",y*10000.0)
elif x=="Hectometro" and z=="Metro":
    print ("El resultado es: ",y*100.0)
elif x=="Hectometro" and z=="Decametro":
    print ("El resultado es: ",y*10.0)
elif x=="Hectometro" and z=="Kilometro":
    print ("El resultado es: ",y/10.0)
elif x=="Kilometro" and z=="Centimetro":
    print ("El resultado es: ",y*100000.0)
elif x=="Kilometro" and z=="Metro":
    print ("El resultado es: ",y*1000.0)
elif x=="Kilometro" and z=="Decametro":
    print ("El resultado es: ",y*100.0)
elif x=="Kilometro" and z=="Hectometro":
    print ("El resultado es: ",y*10.0)
elif x==z:
    print ("La respuesta es la misma debido a que escogio una medida igual")
    
"""

Las opciones son: 

Centrimetro
Metro
Decametro
Hectometro
Kilometro
Indique la medida inicial: Centimetro
Ingrese el valor de la medida: 100
Ingrese a que medida desea convertirlo, seleccione una de la lista dada: Metro
El resultado es:  1

"""
    
        
    
        
    
    
    
