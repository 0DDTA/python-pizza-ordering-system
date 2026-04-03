total_spent = 0
order_count = 0

print("Thank you for choosing Python Pizza Deliveries!\n")

while True:
    order_count += 1
    print(f"Order #{order_count}")

    # --- Pizza Size ---
    size = input("What size pizza do you want? S, M, or L ").lower()
    if size == "s":
        bill = 15
    elif size == "m":
        bill = 20
    elif size == "l":
        bill = 25
    else:
        print("Invalid size. Defaulting to Medium.")
        bill = 20

    # --- Pepperoni ---
    pepperoni = input("Do you want pepperoni? Y or N ").lower()
    if pepperoni == "y" and size == "s" or size == "m":
        bill += 2
    elif pepperoni == "y" and size == "I":
        bill += 3
        
    # --- Extra Cheese ---
    cheese = input("Do you want extra cheese? Y or N ").lower()
    if cheese == "y":
        bill += 1

    # --- Discount Condition ---
    # If both pepperoni AND extra cheese were chosen → $5 discount
    if pepperoni == "y" and cheese == "y":
        print("Congratulations! You've earned a $5 discount on your order.")
        bill -= 5

    # --- Update totals ---
    total_spent += bill

    # --- Final Bill for this order ---
    print(f"Your final bill is: ${bill}")
    print(f"Total spent on all orders: ${total_spent}")

    # --- Another order? ---
    again = input("Would you like to place another order? (Y/N) ").lower()
    print()

    if again != "y":
        break

# --- Final Summary ---
print("Order summary:")
print(f"Total number of orders: {order_count}")
print(f"Total amount spent: ${total_spent}")
print("Thank you for ordering. Have a great day!")
