# Define a function with inputs and a return value
def calculate_total(price, tax_rate=0.05):
    total = price + (price * tax_rate)
    print(total) 

# Call the function
item_cost = calculate_total(100.0)        # Uses default tax_rate of 0.05 -> 105.0
special_cost = calculate_total(100.0, 0.10) # Overrides tax_rate to 0.10 -> 110.0
