import random

def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, introducir un número.")

def intervalo():
    print("Elige tu intervalo:")
    NumInferior = pedir_numero("Numero Inferior: ")
    while True:
        NumSuperior = pedir_numero("Numero Superior: ")
        if NumSuperior <= NumInferior:
            print("El número superior debe ser mayor al primer número.")
        else:
            return NumInferior,NumSuperior
minimo,maximo = intervalo()


def numeroAleatorio(minimo,maximo):
    NumAle = random.randint(minimo,maximo)
    return NumAle
numale = numeroAleatorio(minimo,maximo)


def adivina():
    print("¿Cual es el número?")
    while True:
        NumAdi = pedir_numero("")
        if NumAdi < minimo:
            print("Escoger un número dentro del rango.")
        elif NumAdi > maximo:
            print("Escoger un número dentro del rango.")
        elif minimo <= NumAdi <= maximo:
            return NumAdi

def cercania(adi, minimo, maximo, numale):
    if adi == numale:
        porcentaje = 100
    elif numale == minimo:
        porcentaje = int(abs(maximo-adi)*100/abs(maximo-minimo))
    elif numale == maximo:
        porcentaje = int(abs(adi-minimo)*100/abs(maximo-minimo))
    elif minimo <= adi < numale:
        porcentaje =int((abs(adi-minimo)*100/abs(numale-minimo)))
    elif numale < adi <= maximo:
        porcentaje =int((abs(maximo-adi)*100/abs(maximo-numale)))
    return porcentaje


porcentajes = []
while True:
    adi = adivina()
    resultado = cercania(adi,minimo,maximo,numale)
    if adi == numale:
        break
    porcentajes.append(resultado)
    print(f"Tu numero esta correcto en un {resultado}%.")

Total_intentos = len(porcentajes)
puntajeinicial = 0
for indice,porcentaje in enumerate(porcentajes):
    puntaje = (porcentaje/(2**(indice+1)))
    puntajeinicial = puntajeinicial + puntaje

PuntajeTotal = puntajeinicial + 100/2**(Total_intentos)
print(f"Correcto, tu puntaje es: {"%0.2f"%(PuntajeTotal)}.")