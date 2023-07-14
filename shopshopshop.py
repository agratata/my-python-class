def take_order():
    customer_name = input("Enter your name: ")
    print("Pizza Menu:")
    print("1. Margherita")
    print("2. Pepperoni")
    print("3. Hawaiian")
    print("4. Veggie")
    print("5. Custom Pizza")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        toppings = input("Enter your desired toppings (comma-separated): ")
        pizza = "Custom Pizza with " + toppings
    else:
        pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Veggie"]
        pizza = pizzas[choice - 1]

    print(f"You ordered: {pizza}")
    calculate_bill(customer_name, pizza)

def calculate_bill(customer_name, pizza):
    prices = {
        "Margherita": 10,
        "Pepperoni": 12,
        "Hawaiian": 11,
        "Veggie": 9,
        "Custom Pizza": 15
    }
    topping_price = 1
    toppings_count = 0

    if pizza == "Custom Pizza":
        toppings = input("Enter your desired toppings (comma-separated): ")
        toppings_count = len(toppings.split(","))

    bill = prices[pizza] + (topping_price * toppings_count)
    print(f"Bill: ${bill}")

    save_order(customer_name, pizza, bill)

def save_order(customer_name, pizza, bill):
    order = f"Customer Name: {customer_name}\nPizza: {pizza}\nBill: ${bill}\n"

    with open("orders.txt", "a") as file:
        file.write(order)

    print("Order saved!")


take_order()

