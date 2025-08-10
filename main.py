print("Tip Calculator 💰")

# Step 1: Ask for the bill amount
bill = input("Enter the total bill amount (in colones): ")

# Step 2: Ask for the tip percentage
tip_percentage = input("What tip percentage would you like to leave? (e.g., 10): ")

# Step 3: Convert inputs to numbers
bill = float(bill)
tip_percentage = float(tip_percentage)

# Step 4: Calculate the tip and total
tip = bill * (tip_percentage / 100)
total = bill + tip

# Step 5: Display the results
print("\n Summary:")
print(f"Subtotal: ₡{bill:.2f}")
print(f"Tip ({tip_percentage}%): ₡{tip:.2f}")
print(f"Total to pay: ₡{total:.2f}")