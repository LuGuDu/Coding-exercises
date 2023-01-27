#===================================================================
# Calcular la mediana (valor central) de tres números enteros
#===================================================================

v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
v3 = float(input("Valor 3: "))

lista = [v1, v2, v3]

tam = len(lista)
i1 = int(tam/2) - 1
if (tam % 2 == 0):    
    mediana = (lista[i1] + lista[i1+1]) / 2
else:
    mediana = lista[i1+1]

print("Mediana: ", mediana)

