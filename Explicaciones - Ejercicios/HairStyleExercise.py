#Hairstyles

print('Hairstyles available:')
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
print(hairstyles)
print("                      ")

#Prices

print("Hairstyle prices & Average price: ")
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Last week number of cuts  

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices: 
  total_price += price

average_price = total_price / len(prices) # Fórmula de promedio: total / cantidad de elementos | Ejemplo: suma de notas de clase / cantidad de clases
print(average_price)

new_prices = [price - 5 for price in prices] # Create lists using "List Comprehension"

# new_prices = [] # Equivalente a la línea anterior. "Menos elegante"
# for price in prices:
#   new_prices.append(price - 5)

print ("new_prices")

total_revenue = 0

# Weekkley Total Revenue
print("                      ") # Equivalente a print("\n")
print("Weekley total revenue:")
for i in range(len(hairstyles)): # len = length
 total_revenue += prices[i] * last_week[i]
print(total_revenue)

# Average daily revenue 

print("                      ")
print("Average daily revenue:")
average_daily_revenue = total_revenue / 7
print(average_daily_revenue) 

# Haircuts under 30$$$

print("                      ")
print("Hair cuts under $30 !!:")
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)