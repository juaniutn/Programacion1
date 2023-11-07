
def is_mutant(dna):     
    sequences=0
    tiers=len(dna)
    column=len(dna[0])
    directions=[(1, 0), (0, 1), (1, 1), (-1, 1)]

    for i in range(tiers):
        for j in range(column):
            for direction in directions:
                dx,dy=direction
                x,y=i,j
                count=1

                while 0 <=x+dx<tiers and 0<=y+dy<column and dna[x][y]==dna[x+dx][y+dy]:
                    count+=1
                    x+=dx
                    y+=dy

                if count>=4:
                    sequences+=1

                if sequences>1:
                    return True

    return False
"""Funcion para detectar si es mutante en todas sus formas posibles horizon vertic y diagon (es la funcion de arriba este comentario pero me tiraba error por alguna razon)"""

"""Ingreso de adn y ver si es correcto el ingreso"""
adn=[]
for xxx in range(6):
    row=input("Ingrese la fila de la secuencia de ADN: ").upper()
    
    if len(row)==6 and all(base in "ATCG" for base in row):
        adn.append(row)
    else:
        print("Entrada inválida. Por favor, ingrese una fila válida de 6 caracteres (A, T, C, G).")
        exit()

"""respuesta final con verificacion"""
if is_mutant(adn):
    print("El humano es mutante")
else:
    print("El humano no es mutante")
