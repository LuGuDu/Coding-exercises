#===================================================================
#Dadas las edades de una población de 100 personas, que se leerán 
#por teclado, determinar cuántos son menores que 15, cuántos mayores
#que 35 y cuántos están comprendidos entre 18 y 55.
#===================================================================

menores = 0
mayores = 0
medianos = 0

for persona in range(100):
    edad = int(input("Introduzca edad:\n"))
    if(edad<15):
        menores = menores+1
    elif(edad>35):
        mayores = mayores +1
    else:
        medianos = medianos+1

print("Menores: ", menores, "\nMedianos: ", medianos, "\nMayores: ", mayores)