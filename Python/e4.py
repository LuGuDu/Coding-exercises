#===================================================================
# Escribe un algoritmo que convierta pesetas a euros y viceversa.
#===================================================================

conversor = 166.3860

valor = float(input("Cantidad: "))
print("Euros a pesetas: ", valor*conversor)
print("Pesetas a euros: ", valor/conversor)