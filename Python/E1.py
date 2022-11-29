#===============================================================================================================
# Implementar un programa que calcule el valor del número pi aproximándolo mediante la serie de Leibniz:
# pi = 4 ∗ (1 − 1/3 + 1/5 − 1/7 + 1/9 − ...)
# Permitir que el usuario establezca el número de términos a emplear en la aproximación.
#===============================================================================================================

print("=====================")
print("CÁLCULO DEL NÚMERO PI")
print("=====================")

condicion = True
while condicion == True:
    try:
        n = int(input("Introduzca un numero entero positivo mayor que 1: ")) #Número natural
        if n > 0:
            condicion = False
        else:
            print("No has introducido un número entero mayor que 1")
    except Exception:
        print("Error en la introducción de datos")

operacion = 0
count = 0
for i in range(1, n+1, 2):
    if count % 2 != 0:
        i = - (1/i)
    else:
        i = (1/i)
    operacion += i
    count += 1

pi = 4 * operacion
print(pi)
    