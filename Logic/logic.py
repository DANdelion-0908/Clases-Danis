# Pensamiento Lógico
userAge = float(input("Ingresa tu edad: "))

if userAge >= 18:
    print("Puedes pasar")
else:
    print("Fuera de aquí")

if userAge == 0:
    print("Eres un bebé")
elif userAge >= 1 and userAge <= 12:
    print("Eres un niño")
elif userAge >= 13 and userAge <= 17:
    print("Eres un adolescente")
elif userAge >= 18 and userAge <= 55:
    print("Eres un adulto")
elif userAge >= 56 and userAge <= 122:
    print("Eres un anciano")
else:
    print("Edad imposible")