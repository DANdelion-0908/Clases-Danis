# Tipos de datos

# Datos numéricos
dany = 1 # Int - Entero
daniel = 1.5 # Float - Flotante/Decimal

# Datos textuales
Emilio = "Emilio" # String - Cadena de caracteres

dany + daniel # Correcto
dany + Emilio # Error

# Booleanos - ¿Es un país?
taiwan = True # 1
salama = False # 0 - {} - undefined - None

# Operaciones lógicas
# And
taiwan and salama # False
#  1    *     0

# Or
taiwan or salama # True
#  1   +    0

# Estructuras de datos
listas = []
tuplas = ()
conjuntos = set()
diccionarios = {}

# LIFO - Last In First Out - Pilas
listas.append("A")
listas.append("B")

print(listas)

listas.pop()

print(listas)

listas.clear()

print("-----------------------------")

# FIFO - First In First Out - Colas
listas.append("A")
listas.append("B")

print(listas)

listas.pop(0)

print(listas)

print("-----------------------------")

# ----------------------------------
listas = ["A", "B", "C", "A"]
tuplas = ("A", "B", "C", "A")
conjuntos = set(["A", "B", "C", "A"])
conjuntos2 = set(["A", "D", "E"])
diccionarios = {"Letras": "A"}

print(conjuntos.intersection(conjuntos2))