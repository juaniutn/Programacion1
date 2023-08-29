import math
"""
#ej1 y 2
años=int(input("Ingrese cuantos años tiene nuestra computadora "))
años=int(años)
if (años<0):
    print("Ha ocurrido un error, no se pueden introducir numeros negativos")
else:    
    if (años<=2):
        print("el computador es nuevardo")
    else:
        if (años>2):
            print("el computador es viejardo")


#ej 3
n1=input("Ingrese el primer nombre: ")
n2=input("Ingrese el segundo nombre: ")
n1=n1.lower()
n2=n2.lower()
if (n1[0]==n2[0]):
    print("Coincidencia")
else:
    print("No hubo coincidencia profe :C")

#ej 4
elecc=input("Elija su candidato!!" "\n" "Candidato A por el partido rojo" 
            "\n" "Candidato B por el partido verdad" "\n" "Candidato C por el partido azul" 
            "\n" "Presione A B o C para elegir su candidato!! ")
elecc=elecc.lower()   
if (elecc=="a"):
    print("Usted ha votado por el partido rojo")
elif (elecc=="b"):
    print("Usted ha votado al partido por la verdad")
elif (elecc=="c"):
    print("Usted ha votado por el partido azul")
else:
    print("Ha ocurrido un error, verifique si eligio uno de los posibles candidatos")

#ej 5
letra=input("Digite una letra para saber si es vocal o no ")
vocal=["a", "e", "i", "o", "u"]
letra=letra.lower()
if (len(letra)==1):
    if (letra in vocal):
        print("Es una vocal!!")
    else:
        print("No es una vocal")
else:
    print("Ha ocurrido un error, digite una sola letra") 


#ej 6
año=int(input("Digite un año para saber si es bisiesto: "))
if (año%4==0 and (año%100!=0 or año%400==0)):
    print("Es un año bisiesto!")
else:
    print("No es un año bisiesto!")


#ej 7
n=input("Ingrese 3 numeros para saber su menor: ")
if (n[0]>n[1] and n[0]>n[2]):
    print(f"El numero mayor es", n[0])
elif(n[1]>n[0] and n[1]>n[2]):
    print(f"El numero mayor es", n[1])
elif(n[2]>n[0] and n[2]>n[1]):
    print(f"El numero mayor es", n[2])"""

#ej 8

    


    









