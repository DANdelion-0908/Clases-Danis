# Original con error
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

# -------------------------------------------------------------------------------------
# Corregida V1
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
  return favorite_locations

def show_favorite_locations(favorite_locations):
  print("Your favorite locations are: " + favorite_locations)

show_favorite_locations(print_count_locations())
#--------------------------------------------------------------------------------------
# Corregida V2
def print_count_locations():
  print("There are 3 locations")
    
def show_favorite_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
# ------------------------------------------------------------------------------------
# Corregida V3
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()