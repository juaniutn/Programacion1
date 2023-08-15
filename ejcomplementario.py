
"""" Les otorgo un valor a las variables """
numero1=1
numero2=1.1
"""Sumo las variables y las asigno a suma"""
suma=float(numero1+numero2)
""" resto, multiplico y divido"""
resta=float(numero1-numero2)
mult=float(numero1*numero2)
div=float(numero1/numero2)
""" muestro el resultado de las variables""" """poner str en variable, no en el print"""
print("El resultado de la suma es: " + str(suma))
print("El resultado de la resta es: " + str(resta))
print("El resultado de la multiplicacion es: " + str(mult))
print("El resultado de la division es: " + str(div))
"""Asigno mi nombre a una variable llamada igual"""
nombre="Juani,mica,nazareno,mateo,lautaro" 
""" Asigno un precio """
precio=5
""" asigno un descuento """
descuento=0.10
"""aplico el descuento y lo asigno a una nueva variable"""
precio_final=float(precio-(precio*descuento))
"""creo una variable cadena y le asigno la frase"""
cadena=str("utn")
"""creo una variable llamada longitud para medir cadena"""
longitud=len(cadena)
#creo una variable precio le asigno un entero y lo convierto en decimal#
precio=int(5.5)
#concateno las siguientes variables a una variable final#
nombre="juani"
apellido=" lara"
nombre_completo=str(nombre+apellido)
#hago cuentas en la variable edad#
edad=21+5-10
#altura con decimales, luego hago cuentas#
altura=(1.90*4)/3
#transformo mi nombre en mayusculas, al mismo pero en miinusculas#
nombremayu="JUANI"
nombremin=nombremayu.lower
#Transformo mi nombre en mayusculas a minusculas, excepto la primera letra#
punto16=nombremayu[0] + nombremayu[1:].lower()
print (punto16)