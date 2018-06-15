"""
Programa que resuelve ejercicios de caida libre con las formulas basicas.
V=Velocidad Final
Vo=Velocidad Inicial
G=Gravedad 9.8
D=Distancia
T=Tiempo
"""
import math
x="s"
while x=="s" or x=="S":
    n=0
    v=0
    vo=0
    t=0
    g=9.8
    h=0
    r=0
    print ("Programa de caida libre: ")
    print ("1.-V=Vo-G*T")
    print ("2.-V^2=Vo^2-2g*(D)")
    print ("3.-D=Vo*T-1/2G*T^2")
    print ("4.-D=((Vo+V)/2)*T")
    n=input("Indique que ecuacion desea usar: ")
    while int(n)<1 or int(n)>4:
        n=input("Indique que ecuacion desea usar(de la lista): ")
    if int(n)==1:
        vo=input("Ingrese la velocidad inicial: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        v=int(vo)-g*int(t)
        print ("La velocidad final es: ",round(v,3))
    elif int(n)==2:
        vo=input("Ingrese la velocidad inicial: ")
        h=input("Ingrese la distancia recorrida: ")
        while int(h)<=0:
            h=input("Ingrese la distancia recorrida(positiva): ")
        v=math.sqrt(int(vo)**2-2*g*int(h))
        print ("La velocidad final es: ",round(v,3))
    elif int(n)==3:
        vo=input("Ingrese la velocidad inicial: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        h=int(vo)*int(t)+1/2*g*int(t)**2
        print ("La distancia recorrida es: ",round(h,3))
    elif int(n)==4:
        vo=input("Ingrese la velocidad inicial: ")
        v=input("Ingrese la velocidad final: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        h=(((int(v)+int(vo))/2)*int(t))
        print ("La distancia recorrida es: ",round(h,3))
    x=input("Desea usar otra formula(s/n): ")
    
