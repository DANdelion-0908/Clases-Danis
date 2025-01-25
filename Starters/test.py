# Hello World - Usando funciones
def greeting(characterString):
    print(characterString)

for helloWorld in range(10):
    temporalVariable = 0
    greeting("Hello World")

keyLoop: int = 10

while keyLoop >= 0:
    greeting("Hello World")
    print(keyLoop)
    keyLoop -= 1

myList = ["Pan", "Tomate", "Cebolla", "Agua", "Aceite", "Salsa", "Huevos"]

counter = 0
for index, element in enumerate(myList):
    print(index + 1, " ", myList[counter])
counter += 1

myList.append("Once more")

# Manera simple
myList.remove("Pan")
myList.append("Tortilla")

# Manera más correcta
itemToRemove = myList.index("Agua") # Se elimina de manera dinámica el elemento

print(f"Se ha eliminado el elemento {myList[itemToRemove]}.")

myList[itemToRemove] = "Tortilla"

print(myList)

# Manera completamente dinámica

# If - else
itemInput = input("Ingresa el nombre del producto a eliminar: ")

if itemInput in myList:
    itemToRemove = myList.index(itemInput) # Se elimina de manera dinámica el elemento

    print(f"Se ha eliminado el elemento {myList[itemToRemove]}.")

    itemToAddInput = input("Ingresa el nombre del producto a ingresar: ")

    myList[itemToRemove] = itemToAddInput

    print(myList)

else:
    print("Producto no encontrado.")

# if not
itemInput = input("Ingresa el nombre del producto a eliminar: ")

if itemInput not in myList:
    print("Producto no encontrado.")

else:
    itemToRemove = myList.index(itemInput) # Se elimina de manera dinámica el elemento

    print(f"Se ha eliminado el elemento {myList[itemToRemove]}.")

    itemToAddInput = input("Ingresa el nombre del producto a ingresar: ")

    myList[itemToRemove] = itemToAddInput

    print(myList)

# Using loops
keyLoop = True
test = 0

while keyLoop:
    optionVariable = True
    itemInput = input("Ingresa el nombre del producto a eliminar: ")

    if itemInput not in myList:
        print("Producto no encontrado.")

    else:
        itemToRemove = myList.index(itemInput) # Se elimina de manera dinámica el elemento

        print(f"Se ha eliminado el elemento {myList[itemToRemove]}.")

        itemToAddInput = input("Ingresa el nombre del producto a ingresar: ")

        myList[itemToRemove] = itemToAddInput

        print(myList)

    while optionVariable:
        breakOption = input("¿Desea realizar alguna otra acción? Y/N: ")
        
        if breakOption == "N" and breakOption == "n":
            keyLoop = False
            optionVariable = False

        elif breakOption.upper() == "Y":
            optionVariable = False

        else:
            print("Introduce una opción válida")