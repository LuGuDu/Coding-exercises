#===================================================================
# Escriba un programa que permita convertir de unidades a docenas. 
# El programa deberá solicitar el número de unidades y deberá 
# calcular e imprimir el número de docenas completas correspondientes,
# así como el número restante de unidades del total original 
# (no tiene porqué haber siempre un número exacto de docenas.
# #===================================================================

unidades = float(input("Introduce las unidades: \n"))
decenas = unidades/12
resto = unidades%12
print("Decenas: {:.0f}, Resto: {:.0f}".format(decenas, resto))