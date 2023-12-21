# Get the number of items from the user
num_items = int(input("Enter the number of items you are buying: "))

# Define the pricing structure
if num_items < 10:
    cost_per_item = 12
elif 10 <= num_items <= 99:
    cost_per_item = 10
else:
    cost_per_item = 7

# Calculate the total cost
total_cost = num_items * cost_per_item

# Display the total cost
print(f"Total cost for {num_items} items: ${total_cost}")
