# Creamos funcion con argumento "budget"
def print_remaining_budget(budget_2):

# Imprimimos budget se manera dinamica
  print(f"Your remaining budget is : $ {budget_2}")
  
# Creamos segunda funcion 
def deduct_expense(budget_3, expense):
	
	#calculamos presupuesto 
	return budget_3 - expense

# variable se presupuesto 
budget_1 = float(input("Ingresa tu presupuesto: "))

	
#Llamamos a la funcion 

print_remaining_budget(budget_1)

shirt_expense = 9 

#Llamamos a la funcion con los valores 

budget_after_shirt = deduct_expense(budget_1, shirt_expense)

#Llamamos por ultima vez a la funcion despues del gasto

print_remaining_budget(budget_after_shirt)