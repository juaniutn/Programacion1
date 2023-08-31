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
    print(f"El numero mayor es", n[2])

#ej 9
    
nombre=(input("Ingrese su nombre: "))
sexo=input("Ingrese su sexo Masculino o Femenino: ")
nombre=nombre.lower()
sexo=sexo.lower()

if((nombre[0]<"m" and sexo=="femenino") or (nombre[0]>"n" and sexo=="masculino")):
    print ("Perteneces al grupo A")
else:
    print ("Perteneces al grupo B")

#ej 8

usuario=input("Ingrese su usuario: ")
contra=input("Ingrese su contraseña: ")
if((usuario=="Gwenevere") and (contra=="excalibur")):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado") 

#ej 10


edad=int(input("Ingrese su edad: "))
if(edad<4):
    print("Puede entrar gratis")
elif(edad>3 and edad<19):
    print("Debe pagar $500")
elif(edad>18):
    print("Debe pagar $1000")

#ej 11



print("¿Qué tipo de pizza le gustaría?")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")

opcion = int(input("Ingrese el número de su elección: "))

if opcion == 1:
    print("Ingredientes disponibles para la pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente = int(input("Seleccione un ingrediente (1 o 2): "))
    if ingrediente == 1:
        ingredientes_elegidos = ["Mozzarella", "Tomate", "Pimiento"]
    elif ingrediente == 2:
        ingredientes_elegidos = ["Mozzarella", "Tomate", "Tofu"]
    tipo_pizza = "vegetariana"
elif opcion == 2:
    print("Ingredientes disponibles para la pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    ingrediente = int(input("Seleccione un ingrediente (1, 2 o 3): "))
    if ingrediente == 1:
        ingredientes_elegidos = ["Mozzarella", "Tomate", "Peperoni"]
    elif ingrediente == 2:
        ingredientes_elegidos = ["Mozzarella", "Tomate", "Jamón"]
    elif ingrediente == 3:
        ingredientes_elegidos = ["Mozzarella", "Tomate", "Salmón"]
    tipo_pizza = "no vegetariana"
else:
    print("Opción inválida")

if opcion == 1 or opcion == 2:
    print(f"Usted ha elegido una pizza {tipo_pizza} con los siguientes ingredientes:")
    for ingrediente in ingredientes_elegidos:
        print(ingrediente) 
#ej 12
actual=int(input("Ingrese el año actual: "))
otro=int(input("Ingrese el año siguiente: "))
if(actual>otro):
    print("Faltan ", actual-otro, " años para llegar a ", actual, " desde ", otro)
elif(actual<otro):
     print("Faltan ", otro-actual, " años para llegar a ", otro, " desde ", actual)
elif(actual==otro):
     print("Es el mismo año") 

#ej 13

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))

if num1 <= 0 or num2 <= 0:
    print("Por favor, ingrese números enteros positivos.")
elif num1 > num2 and num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}.")
elif num2 > num1 and num2 % num1 == 0:
    print(f"{num2} es múltiplo de {num1}.")
else:
    print("El mayor no es múltiplo del menor.") 

#ej 14
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))


if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}") 
#ej 15

opcion = input("¿Quieres calcular el área de un triángulo (T) o un círculo (C)? ")


opcion = opcion.lower()

if opcion == "t":

    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area_triangulo = 0.5 * base * altura
    print(f"El área del triángulo es: {area_triangulo}")
elif opcion == "c":
 
    radio = float(input("Introduce el radio del círculo: "))
    area_circulo = 3.14159 * radio ** 2
    print(f"El área del círculo es: {area_circulo}")
else:
    print("Opción no válida. Debes elegir 'T' o 'C'.") 

#ej 16


a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))


print("Seleccione la operación:")
print("1. Suma")
print("2. Multiplicación")
print("3. Resta")
print("4. División")

opcion = int(input("Ingrese el número de la operación deseada: "))


if opcion == 1:
    resultado = a + b
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = a * b
    print("El resultado de la multiplicación es:", resultado)
elif opcion == 3:
    resultado = a - b
    print("El resultado de la resta es:", resultado)
elif opcion == 4:
    if b != 0:  
        resultado = a / b
        print("El resultado de la división es:", resultado)
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.") 

# ej 17

dia=str(input("Ingrese un dia de la semana: "))
dia=dia.lower()
if(dia=="lunes"):
    print("Buen lunes!!")
elif(dia=="viernes"):
    print("Buen viernes")
elif(dia=="sabado" or dia=="domingo"):
    print("Buen finde!")
elif(dia=="martes" or dia=="miercoles" or dia=="jueves"):
    print("buen entresemana!")
else:
    print("No ingreso un dia de la semana") 

# ej 18

horastotales=int(input("Cuantas horas trabajo este mes?: "))
salarioxhora=int(input("De cuanto es su salario por hora?: "))
if(horastotales<=48):
    print("Su salario total es de: ", horastotales*salarioxhora)
elif(horastotales>48):
    print("Su salario total es de: ", (48*salarioxhora)+((horastotales-48)*(salarioxhora*1.1))) 

#ej 19

costo=60
lapices=int(input("Cuantos lapices desea comprar?: "))
if(lapices>=1000):
    print("El costo total es de: ", (lapices*costo)*0.93)
else:
    print("El costo total es de: ", lapices*costo) 

#ej 20


nota1=5
nota2=4
nota3=3
nota4=2
if((nota1+nota2+nota3+nota4)/4>=6):
    print("Aprobado")
else:
    print("Desaprobado") """


          







    









