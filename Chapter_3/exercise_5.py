### program: To find total cost of the order

def order_cost(pounds):
    total_cost = 10.5 * pounds + 0.86 * pounds + 1.50
    print("Total cost for your order:", total_cost, "dollars")

weight = float(input("Enter the weight of coffee you want to order (in pounds): "))
order_cost(weight)
