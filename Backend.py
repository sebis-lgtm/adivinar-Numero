#No probe con numeros negativos todavia xde
#Tengo que hacer que si no introducen algo que no es un numero salga un aviso.

import random

def intervalo():
    print("Elige tu intervalo:")
    NumInferior = int(input("Numero menor:"))
    NumSuperior = int(input("Numero mayor:"))
    return NumInferior,NumSuperior
minimo,maximo = intervalo()


def numeroAleatorio(minimo,maximo):
    NumAle = random.randint(minimo,maximo)
    return NumAle
numale = numeroAleatorio(minimo,maximo)


def adivina():
    print("¿Cual es el numero?")
    NumAdi = int(input())
    if NumAdi < minimo:
        print("Escoger un numero dentro del rango.")
        adivina()
    if NumAdi > maximo:
        print("Escoger un numero dentro del rango.")
        adivina()
    return NumAdi

def cercania(adi, minimo, maximo, numale):
    if minimo <= adi < numale:
        porcentaje =int(((adi-minimo)*100/(numale-minimo)))
    elif numale < adi <= maximo:
        porcentaje =int(((maximo-adi)*100/(maximo-numale)))
    elif adi == numale:
        porcentaje = 100
    return porcentaje


porcentajes = []
while True:
    adi = adivina()
    resultado = cercania(adi,minimo,maximo,numale)
    if adi == numale:
        break
    porcentajes.append(resultado)
    print(f"Tu numero esta correcto en un {resultado}%")

Total_intentos = len(porcentajes)
puntajeinicial = 0
for indice,porcentaje in enumerate(porcentajes):
    puntaje = (porcentaje/(2**(indice+1)))
    puntajeinicial = puntajeinicial + puntaje

PuntajeTotal = puntajeinicial + 100/2**(Total_intentos)
print(PuntajeTotal)