def clean_window():
    print("========================================")

def menu():
    print("BIENVENIDOS AL SISTEMA DE ADIVINAR NúMERO")
    print("==============MENU==============")
    print("1.Nivel fácil (1 - 10)")
    print("2.Nivel medio (1 - 50)")
    print("3.Nivel dificil (1 - 100)")
    level  = input("Elija una opción -> ")
    game(level)  

def generate_number(level):
    # number = generate(level)
    # return number
    return 1

def game(level):
    clean_window()
    print(f"NIVEL {level}")
    number = generate_number(level)
    iteration(number)

def input_number():
    return int(input("Ingresa un número -> "))

def finish_game(result, number):
    if result:
        print("GANASTE!!!")
    else:
        print(f"FALLASTE EL NUMERO ERA -> {number}")

def iteration(number):
    oportunities = 3
    for oportunity in range (oportunities):
        number_select = input_number()
        if number_select == number:
            finish_game(True, number)
            return
        elif number_select > number:
            print("El número es menor")
        else: 
            print("El número es mayor")
    
    if oportunity == oportunities - 1:
        finish_game(False, number)

def start():
    menu()

if __name__ == "__main__":
    start()