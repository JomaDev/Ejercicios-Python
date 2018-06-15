#Juego_de_Azar.py
"""
Programa que captura un número de 1 a 100 y da al usuario la oportunidad de
adivinar cual numero es. El usuario tiene 5 intentos para adivinar.
"""
import random
x=0
z=0
print("Juego de Azar")
y=input("Ingrese su nombre ")
a=random.randint(1,100)
print ("Hola", y,"Empecemos el juego")
print ("El juego consiste en que adivine que número he pensado entre 1 a 100")

while x<5 and z!=a:
    z=int(input("Ingrese el número que cree que es: "))
    if z<a:
        print ("Mi número es más alto")
    elif z>a:
        print ("Mi número es mas pequeño")
    x=x+1
    
if z==a:
    print (y,"Ganaste en", x, "intentos")
else:
    print (y,"Perdiste era:",a)
        
