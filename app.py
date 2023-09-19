from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample menu items and prices
menu = {
    '1': {'name': 'Hamburger', 'price': 5.99},
    '2': {'name': 'Cheeseburger', 'price': 6.49},
    '3': {'name': 'Chicken Sandwich', 'price': 7.99},
    '4': {'name': 'French Fries', 'price': 2.49},
    '5': {'name': 'Soda', 'price': 1.49},
}

# Create a global variable to store the order
order = {}

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    item_num = request.form.get('item_num')
    quantity = int(request.form.get('quantity'))

    if item_num in menu:
        if item_num in order:
            order[item_num]['quantity'] += quantity
        else:
            order[item_num] = {'name': menu[item_num]['name'], 'price': menu[item_num]['price'], 'quantity': quantity}

    return redirect(url_for('index'))

@app.route('/confirmation')
def confirmation():
    total_cost = calculate_total(order)
    return render_template('receipt.html', order=order, total_cost=total_cost)

def calculate_total(order):
    total = 0
    for item_info in order.values():
        total += item_info['price'] * item_info['quantity']
    return total

if __name__ == '__main__':
    app.run(debug=True)
