# Los parámetros son datos que pasamos a las funciones para que los utilicen en su código.
# def trip_welcome(origin, destination):
#   print("Welcome to Tripcademy")
#   print("Looks like you are traveling from " + origin)
#   print("And you are heading to " + destination)

# trip_welcome("Guatemala", "Israel")
# # ----------------------------------------------------------------------------------------------
# # Ejemplo dinámico
# originCountry = input("\nIngresa el país del que vienes: ")
# destinationCountry = input("\nIngresa el país al que vas: ")

# trip_welcome(originCountry, destinationCountry)
# ----------------------------------------------------------------------------------------------
def multipleExample(variableOne, variableTwo):
  print(f"{variableOne} and {variableTwo}")

multipleExample("5", "1") # Posicional
multipleExample("1", "5")

multipleExample(variableOne="5", variableTwo="1") # Keyword
multipleExample(variableTwo="1", variableOne="5")