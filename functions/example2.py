# Pedimos al usuario su presupuesto inicial
current_budget = input("Ingrese su presupuesto inicial: ")

if (current_budget.isnumeric()):
    float(current_budget)

else:
    print("Ingresa un tipo de dato válido.")

# Función para imprimir el presupuesto restante
def print_remaining_budget(budget):
    print(f"Your remaining budget is: $ {budget:.2f}")

# Función para restar un gasto del presupuesto
def deduct_expense(current_budget, expense):
    return current_budget - expense

# Mostramos el presupuesto inicial
if (current_budget.isnumeric()):
    print_remaining_budget(current_budget)

else:
    print("Ingresa un tipo de dato válido.")

# Bucle para ingresar múltiples gastos
while True:
    expense = input("Ingrese el monto del gasto (o escriba 'salir' para finalizar): ")
    
    if expense.lower() == "salir":
        break  # Salimos del bucle si el usuario escribe "salir"
    
    try:
        expense = float(expense)  # Convertimos la entrada en un número
        current_budget = deduct_expense(current_budget, expense)  # Restamos el gasto
        print_remaining_budget(current_budget)  # Mostramos el presupuesto actualizado
    except ValueError:
        print("Por favor, ingrese un número válido.")  # Mensaje de error si la entrada no es válida

# Mensaje final
print("Gestión de presupuesto finalizada.")