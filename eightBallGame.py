# 8 BALL EXERCISE

import random

# Pedir el nombre del usuario
user_name = input("Please enter your name ✨🔮: ")
print(f"\nNice to meet you, {user_name}! ♥️")

# Definir la función de respuestas
def Answers():
    options = [
        "It is certain 🙈",
        "It is decidedly so 😏☺️",
        "Without a doubt 😎",
        "Yes – definitely 😌😌😌",
        "You may rely on it 💯",
        "As I see it, yes 🤷‍♂️",
        "Most likely 😜",
        "Outlook good 😬👌",
        "Yes 🫡",
        "Signs point to yes 🫡👌",
        "Reply hazy, try again 🤷‍♂️",
        "Ask again later 🤔",
        "Better not tell you now 😰😱",
        "Cannot predict now 🫠",
        "Concentrate and ask again 😮‍💨🤯",
        "Don't count on it 😭😤",
        "My reply is no 👀😌",
        "My sources say no 😅😮",
        "Outlook not so good 🫠",
        "Very doubtful 🥶🥶🥶",
        "I can't take the question seriously, sorry 😂🤷‍♂️"
    ]
    return random.choice(options)

# Bucle principal del programa
while True:
    # Preguntar al usuario su pregunta
    message_to_8ball = input("\nAsk the Magic 8 Ball a question: ")

    input("\nPress ENTER to start your Fortune-telling...")

    # Mostrar respuesta aleatoria
    print("\n🔮 The Magic 8 Ball says:", Answers())

    # Preguntar si quiere salir o continuar
    close = input("\nType 'exit' or 'finish' to quit, or 'try again' to ask another question: ").lower() # Exit -> exit

    # Condición para salir del bucle
    if close == "exit" or close == "finish":
        print("\nHave a superb day! 🔮")
        break  # Se detiene el bucle