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
    print("Ha ocurrido un error, verifique si eligio uno de los posibles candidatos")"""

#ej 5
letra=input("Digite una letra para saber si es vocal o no ")
vocal=["a", "e", "i", "o", "u"]
letra=letra.lower()
if (len(letra)>0):
    if (letra in vocal):
        print("Es una vocal!!")
    else:
        print("No es una vocal")
else:
    print("Ha ocurrido un error, digite una sola letra")

    









