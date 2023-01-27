#===================================================================
#Determinar el precio de un billete de ida y vuelta en autobús 
# teniendo en cuenta que dicho precio depende de la distancia a 
# recorrer y del número de días entre trayectos:
#      - El precio del kilómetro es de 50 cts. de euro
#      - Si la distancia es superior a 800 kms. y el número 
#        de días entre la fecha de ida y la de vuelta es inferior 
#        a 5, el precio del billete tiene una reducción del 30%
#===================================================================

precio_kilometro = 0.5

precio_final = 0
distancia = float(input("Introduzca la distancia: \n"))
dias = float(input("Introduzca los dias totales: \n"))

precio_final = distancia * precio_kilometro
if (distancia>800 and dias>5):
    precio_final = precio_final*0.7

print(precio_final,"€")