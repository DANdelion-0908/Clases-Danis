# variable1 = range(5)
# listExample = ["a", "b", "c"]
# variable2 = len(listExample)

# print(variable2)

# #Eliminar todos los elementos de la lista
# while len(listExample) != 0:
#     print(listExample.pop())

# print("")

# while listExample:
#     print(listExample.pop())

# print(listExample.pop(1)) # Eliminar elemento con índice 1

# P.D.: POP elimina el último por defecto, a menos que lo indiques

# ----------------------------------------------------------------------------------------------------------
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_revenue = 0

lenFormat = len(hairstyles)
rangeFormat = range(8)

for i in rangeFormat:
    print(f"Elemento No. {i}")

# print(f"Range: {rangeFormat} ", f"Len: {lenFormat}")

# print("Weekley total revenue:")
# for i in range(len(hairstyles)): # len = length
#  total_revenue += prices[i] * last_week[i]
# print(total_revenue)