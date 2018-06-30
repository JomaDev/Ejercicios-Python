#Operaciones.py
"""
Haga un men� con 7 opciones: suma,resta,multiplicacion,division,potencia,raiz y fin.
Cada una de las opercaciones debe ser una funci�n
"""
import math          #Importamos math para la ra�z
a=0
b=0                               #Definir variables globales
s=0
x=0
i=" "
q=0
n=0
r=0
def su(a,b):
    a=int(input("Ingrese primer valor a sumar:"))              #Definir funci�nes
    b=int(input("Ingrese segundo valor a sumar:"))
    s=a+b
    return s
def re(a,b):
    a=int(input("Ingrese primer valor:"))
    b=int(input("Ingrese ingrese el valor que restara:"))
    s=a-b
    return s
def mu(a,b):
    a=int(input("Ingrese primer:"))
    b=int(input("Ingrese el que multiplicara:"))
    s=a*b
    return s
def di(a,b):
    a=int(input("Ingrese el dividendo:"))
    b=int(input("Ingrese el divisor:"))
    while a==0 or b==0:
        a=int(input("Ingrese dividendo diferente de 0:" ))
        b=int(input("Ingrese divisor diferente de 0:"))
    s=a/b
    return s
def po(a,b):
    a=int(input("Ingrese primer valor:" ))
    b=int(input("Ingrese a que potencia se elevara:"))
    s=a**b
    return s
def ra(a):
    a=int(input("Ingrese valor: "))
    s=math.sqrt(a)
    return s
    
while x!=7:
    x=0
    list=["1.-SUMA","2.-RESTA","3.-MULTIPLICACION","4.-DIVISION","5.-POTENCIA","6.-RAIZ","7.-FIN"]
    for i in list:
        print (i)
    while x<1 or x>7:                       #Comprobar que es un numero de la lista
        x=int(input("Ingrese la operacion que desea realizar:"))
    if x==1:
        q=su(a,b)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
            
    elif x==2:
        q=re(a,b)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
    elif x==3:
        q=mu(a,b)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
    elif x==4:
        q=di(a,b)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
    elif x==5:
        q=po(a,b)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
    elif x==6:
        q=round(ra(a),2)
        r=int(input("Ingrese la posible respuesta: "))
        if q==r:
            print ("Acerto es:",q)
        else:
            print ("No es correcto, era:",q)
    elif x==7:
        print ("Indico acabar programa")
    


"""
1.-SUMA
2.-RESTA
5.-MULTIPLICACION
4.-DIVISION
5.-POTENCIA
6.-RAIZ
7.-FIN
Ingrese la operaci�n que desea realizar:1
Ingrese primer valor a sumar:50
Ingrese segundo valor a sumar:-20
La suma de los n�mero es:  30
"""
