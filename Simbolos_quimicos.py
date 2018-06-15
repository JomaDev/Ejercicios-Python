# -*- coding: cp1252 -*-
#Simbolos_quimicos.py
"""
Programa que muestra el simbolo del elemento quimico, en la pantalla que muestre una relacion de 10 elementos quimicos, luego que permita escoger uno de ellos
y debe mostar el simbolo del elemento
"""
x=""
y=1
while y==1:
    list=["Potasio","Oro","Plata","Cobre","Paladio","Azufre","Hidrogeno","Helio","Oxigeno","Hierro"]           #Creamos una lista para mostras los 10 elementos
    for x in list:
        print (x)
    x=input("Indique el elemento que desea ")            #Usamos raw_input para poder escribir una cadena de letras
    if x=="Potasio" or x=="potasio":
        print ("El elemento es:",x," y su simbolo es: K")        #Usamos ef y else para poder definir los simbolos
    else:
        if x=="Oro" or x=="oro" :
            print ("El elemento es:",x," y su simbolo es: Au")                
        else:
            if x=="Plata" or x=="plata":
                print ("El elemento es:",x," y su simbolo es: Ag")                         
            else:
                if x=="Cobre" or x=="cobre":
                        print ("El elemento es:",x," y su simbolo es: Cu")
                else:
                    if x=="Paladio" or x=="paladio":
                            print ("El elemento es:",x," y su simbolo es: Pl")
                    else:
                        if x=="Azufre" or x=="azufre":
                            print ("El elemento es:",x," y su simbolo es: S")
                        else:
                            if x=="Hidrogeno" or x=="hidrogeno":
                                print ("El elemento es:",x," y su simbolo es: H")
                            else:
                                if x=="Helio" or x=="helio":
                                     print ("El elemento es:",x," y su simbolo es: He")
                                else:
                                    if x=="Oxigeno" or x=="oxigeno":
                                         print ("El elemento es:",x," y su simbolo es: O")
                                    else:
                                        if x=="Hierro" or x=="hierro":
                                             print ("El elemento es:",x," y su simbolo es: Fe")
    y=int(input("Desea seleccionar otro elemento: (1=Si/0=No)"))                                       
                                
                        
        

    
