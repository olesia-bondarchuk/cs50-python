# Greet customer, ask what item does he want:
# -----Select 1 for coke, Select 2 - Lays, Select 3 - Snickers
# Print table of available items, their code, name and price
# If unknown option - let him know and abort
# Do same as coke.py
# Price for coke - 50c, Lays  - 70, Snickers - 60
# Print "Enjoy your __SELECTED_ITEM__"

from typing import Dict

# Frontend (vending machine itself)
def main():
    print("Hello! Please select from the options below:")
    available_products = get_available_products()
    for place in available_products:
        print(f"For {available_products[place]} press '{place}' ({get_price(available_products[place])}¢)")
    
    option = input("")
    product_name = get_product_name(option)
    if product_name == None:
        print("No such option!")
        return -1
    
    price = get_price(product_name)
    if price == -1:
        print("Not available!")
        return -2
    
    amount = ask_for_money(price)
    change = calculate_change(price, amount)
    if change > 0:
        print(f"Get your change: {change}¢")
    
    print(f"Enjoy your {product_name}")
    return 0

def get_available_products() -> Dict[str, str]:
    return {"1": "Coke", "2": "Lays", "3": "Snickers"}


def get_product_name(place: str) -> str:
    name_table = get_available_products()
    if place not in name_table:
        return None
    else:
        return name_table[place]

def ask_for_money(expected_amount: int) -> int:
    acceptable_coins = [5, 10, 25]
    acceptable_coins_str = ", ".join([str(i) for i in acceptable_coins])
    amount = 0
    while amount < expected_amount:
        coin = int(input(f"Amount due: {expected_amount - amount}¢. Insert a coin (acceptable coins {acceptable_coins_str}): "))
        if coin not in acceptable_coins:
            print("Invalid coin.")
            continue

        amount = amount + coin
    
    return amount

def calculate_change(expected_amount: int, actual_amount: int) -> int:
    return actual_amount - expected_amount

#server part
def get_price(product: str) -> int: 
    product_prices = {"coke": 50, "lays": 70, "snickers": 60}
    product = product.lower()

    if product not in product_prices:
        return -1
    else:
        return product_prices[product]



if __name__ == "__main__":
    main()