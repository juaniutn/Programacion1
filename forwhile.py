
#1
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word=input("Escriba su palabra a encriptar: ")
word=word.lower()
long=int(input("Cuantos lugares quiere correr en su encriptado?: "))
longword=len(word)
for i in range(0,longword,1):
    if(word.isalpha()):
        position=abc.index(word[i])
        showedword=abc[(position+long)%27]
        print(f"{showedword}", end="")
    else:
        print(word[i])


#2
num=int(input("Ingrese un numero positivo: "))
numpair=0
numimpair=0
numpairtotal=0
numimpairtotal=0
while (num!=0):
    nums=str(num)
    long=len(nums)
    for i in range(0,long, 1):
        numif=nums[i]
        numif=int(numif)
        if(numif==0):
            numpair=numpair+1
        elif(numif%2==0):
            numpair=numpair+1
        elif(numif%2!=0):
            numimpair=numimpair+1
    numpairtotal=numpairtotal+numpair
    numimpairtotal=numimpair+numimpairtotal
    print ("Cantidad de numeros impares: ", numimpair)
    print (f"Cantidad de numeros pares: {numpair}")
    numpair=0
    numimpair=0
    num=int(input("Ingrese un numero posiivo: "))
    
print(f"La cantidad total de numeros pares es: {numpairtotal}")
print(f"La cantidad total de numeros impares es: {numimpairtotal}")

    


    