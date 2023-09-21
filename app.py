from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu = {
    '1': {'name': 'Hamburger', 'price': 5.99, 'image': 'Hamburger.jpeg'},
    '2': {'name': 'Cheeseburger', 'price': 6.49, 'image': 'Cheeseburger.jpeg'},
    '3': {'name': 'Chicken Sandwich', 'price': 7.99, 'image': 'Chicken_sandwich.jpeg'},
    '4': {'name': 'French Fries', 'price': 2.49, 'image': 'Frenchfries.jpeg'},
    '5': {'name': 'Soda', 'price': 1.49, 'image': 'Soda.jpeg'},
}

order = {}

@app.route('/', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        for item_num, quantity in request.form.items():
            if item_num.startswith('quantity_'):
                item_num = item_num.replace('quantity_', '')
                try:
                    quantity = int(quantity)
                    if quantity <= 0:
                        continue
                    
                    if item_num in menu:
                        if item_num in order:
                            order[item_num]['quantity'] += quantity
                        else:
                            order[item_num] = {'name': menu[item_num]['name'], 'price': menu[item_num]['price'], 'quantity': quantity}
                except ValueError:
                    pass

        total_cost = round(calculate_total(order),2)
        return render_template('receipt.html', order=order, total_cost=total_cost)

    return render_template('index.html', menu=menu)

def calculate_total(order):
    total = 0
    for item_info in order.values():
        total += item_info['price'] * item_info['quantity']
    return total

if __name__ == '__main__':
    app.run(debug=True)
