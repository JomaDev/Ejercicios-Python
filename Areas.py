#Programafigura.py
"""
#Programa que muestra un menu, cada numero representa una figura geometrica en el siguiente orden:
1.-Cuadrado
2.-Rectangulo
3.-Triangulo
4.-Circulo
5.-Trapecio
6-Rombo
Luego que ingrese la opcion, la cual debe ser enviada a una funcion que calcule el area correspondiente
"""
x=0                #Definir variables
y=" "
z=0
pi=3.14
l=0
a=0
b=0
c=0
w="s"
def cu(l):
      l=int(input("Ingrese lado del cuadrado: "))         #Definimos funciones
      z=l*l
      return z
def re(a,b):
      a=int(input("Ingrese medida de la base: "))
      b=int(input("Ingrese medida de la altura: "))
      z=a*b
      return z
     
def tri(a,b):
      a=int(input("Ingrese medida de la altura: "))
      b=int(input("Ingrese medida de la base: "))
      z=(a*b)/2
      return z
      
def ci(a):
      a=int(input("Ingrese medida del radio del circulo: "))
      z=pi*(a*a)
      return z
      
def tra(a,b,c):
      a=int(input("Ingrese medida de la base mayor: "))
      b=int(input("Ingrese medida de la base menor: "))
      c=int(input("Ingrese medida de la altura: "))
      z=((a+b)*c)/2
      return z
      
def ro(a,b):
      a=int(input("Ingrese medida de la diagonal mayor: "))
      b=int(input("Ingrese medida de la diagonal menor: "))
      z=(a*b)/2
      return z
      
while w=="s" or w=="S":
    list=["1.-Cuadrado","2.-Rectangulo","3.-Triangulo","4.-Circulo","5.-Trapecio","6.-Rombo"]
    for y in list:
         print (y)
    x=int(input("Ingrese el numero de la figura que desea: "))
    while x<1 or x>6:
        x=int(input("Ingrese el numero de la lista : "))
    
    if x==1:                    #Llamar funciones 
      q=cu(l)
      print ("El valor retornado es: ",q)
    elif x==2:
      q=re(a,b)
      print ("El valor retornado es: ",q)
    elif x==3:
      q=tri(a,b)
      print ("El valor retornado es: ",q)
    elif x==4:
      q=ci(a)
      print ("El valor retornado es: ",q)
    elif x==5:
      q=tra(a,b,c)
      print ("El valor retornado es: ",q)
    elif x==6:
      q=ro(a,b)
      print ("El valor retornado es: ",q)
    w=input("Desea continuar (s/n): ")
    if w=="n" or w=="N":
        print ("Acabo programa")
"""
>>> 
1.-Cuadrado
2.-Rectangulo
3.-Triangulo
4.-Circulo
5.-Trapecio
6.-Rombo
Ingrese el numero de la figura que desea: 1
Ingrese lado del cuadrado: 5
El valor retornado es:  25
Desea continuar (s/n): s
1.-Cuadrado
2.-Rectangulo
3.-Triangulo
4.-Circulo
5.-Trapecio
6.-Rombo
Ingrese el numero de la figura que desea: 4
Ingrese medida del radio del circulo: 10
El valor retornado es:  314.0
Desea continuar (s/n): n
Acabo programa
>>>
"""
      
