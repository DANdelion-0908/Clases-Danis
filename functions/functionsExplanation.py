import functionDefinition

# Funciones. Bloques de código que realizan una tarea específica. Pueden recibir variables como parámetros y retornar otras variables.
# Como caso de uso ideal, se utilizan cuando necesitas hacer algo varias veces.

# print("Checking the weather for you!")

# def weather_check(): # El chiste de las funcciones es llamarlas en cualquier lugar del código para que realicen su tarea.
#     print("Looks great outside! Enjoy your trip.")
#     print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

# #Printing function 
# weather_check()
#-------------------------------------------------------------------------------------------------------------------------------------------------

PI = 3.1416
radio = float(input("Ingrese el radio del círculo en cm: "))

def getArea():
    result = PI * pow(radio, 2)
    return result

variable = getArea()

print(variable)