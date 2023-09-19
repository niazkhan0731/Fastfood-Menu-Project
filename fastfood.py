# Sample menu items and prices
menu = {
    '1': {'name': 'Hamburger', 'price': 5.99},
    '2': {'name': 'Cheeseburger', 'price': 6.49},
    '3': {'name': 'Chicken Sandwich', 'price': 7.99},
    '4': {'name': 'French Fries', 'price': 2.49},
    '5': {'name': 'Soda', 'price': 1.49},
}

# Function to display the menu
def display_menu():
    print("Menu:")
    for item_num, item_info in menu.items():
        print(f"{item_num}: {item_info['name']} - ${item_info['price']}")

# Function to take customer orders
def take_order():
    order = {}
    while True:
        display_menu()
        item_num = input("Enter the item number to add to your order (0 to finish): ")
        if item_num == '0':
            break
        elif item_num in menu:
            quantity = int(input(f"Enter the quantity of {menu[item_num]['name']} you want: "))
            if item_num in order:
                order[item_num]['quantity'] += quantity
            else:
                order[item_num] = {'name': menu[item_num]['name'], 'price': menu[item_num]['price'], 'quantity': quantity}
        else:
            print("Invalid item number. Please select a valid item.")
    return order

# Function to calculate the total cost of the order
def calculate_total(order):
    total = 0
    for item_info in order.values():
        total += item_info['price'] * item_info['quantity']
    return total

# Main ordering process
if __name__ == "__main__":
    print("Welcome to the Fast Food Ordering System!")
    customer_order = take_order()

    if not customer_order:
        print("No items in the order. Thank you for visiting.")
    else:
        print("\nOrder Summary:")
        for item_num, item_info in customer_order.items():
            print(f"{item_info['name']} - ${item_info['price']} x{item_info['quantity']}")

        total_cost = calculate_total(customer_order)
        print(f"\nTotal: ${total_cost:.2f}")
        print("Thank you for your order. Enjoy your meal!")