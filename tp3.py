
#ej 1
"""
word=input("Ingrese una palabra: ")
for i in range(10):
    print(word) 
#ej 2

age=int(input("Digite su edad "))
for i in range(age):
    print(i+1) """

#ej 3
""" ⦁	Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
 """
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    impares = []

    for i in range(1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    
    resultado = ', '.join(impares)
    print(resultado)







    

       


   

