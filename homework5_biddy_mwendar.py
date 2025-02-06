# List Exercise

# Create a list with 6 car models
car_models = ["Tesla", "Isuzu", "Toyota", "Mercedes", "Volkswagen", "Honda"]

# Print all items in the list
print("The car models in the list are:", car_models)

# Print the first two items using a slice
print(f"The first two items in the list are: {car_models[0]}, {car_models[1]}")

# Print the middle two items using a slice
print(f"The middle two items in the list are: {car_models[2]}, {car_models[3]}")

# Print the first and last items using indexes
print(f"The first and last items in the list are: {car_models[0]}, {car_models[-1]}")

# Tuple Exercise

# Create a tuple with five menu items
menu = ("Bruschetta", "Spring Rolls", "Sashimi", "Lobster", "Brownies")

# Print each item on the menu using a for loop 
print("Original menu:")
for item in menu:
    print(item)

# Update the menu by creating a new tuple with two replaced items
updated_menu = ("Bruschetta", "Spring Rolls", "Grilled Salmon", "Steak", "Brownies")

# Print the revised menu using a while loop 
print("Updated menu:")
i = 0
while i < len(updated_menu):
    print(updated_menu[i])
    i += 1
