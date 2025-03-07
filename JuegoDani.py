Dani = 1000
DaniAttack = 50
Inad = 1000

def Lanzallamas(condition, Dani):
    if condition < 950: 
        print("El dragón lanzó fuego y te hizo 500 puntos de daño") 
        Dani -= 500

    else:
        print("El lanzallamas falló")

    return Dani

while Dani > 0 and Inad > 0:
    action = input("1. Atacar | 2. Usar Objeto | 3. Rendirse")

    if action == "1":
        Inad -= DaniAttack
        print(f"Atacaste al Inad y ahora tiene {Inad} puntos de vida")

    elif action == "2":
        item = input("1. Red Bull | 2. Bomba | 3. Monster")
        if item == "1":
            Dani += 100

        elif item == "2":
            Inad -= 300

        elif item == "3":
            DaniAttack += 20

    Dani -= 150
    print(f"Inad ataca y ahora tienes {Dani} puntos de vida")
    Dani = Lanzallamas(Inad, Dani)

print("Perdiste")
