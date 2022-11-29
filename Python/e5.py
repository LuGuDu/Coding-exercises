#===================================================================
# Escriba un programa que convierta de grados centígrados a Fahrenheit
#===================================================================

def CelToFah(valor):
    fah = (valor * 1.8)+32
    return fah

def FahToCel(valor):
    cel = (valor-32)/1.8
    return cel

valor = float(input("Temperatura: "))
print("Celsius a Fahrenheit: ", CelToFah(valor))
print("Fahrenheit a Celsius: ", FahToCel(valor))