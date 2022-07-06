amount = 0
while amount < 50:
    print(f"Amount Due: {50 - amount}")
    coin = int(input("Insert a coin (only 5c, 10c, 25c): "))
    if coin !=5 and coin !=10 and coin !=25:
        print(f"{coin} is not a valid coin")
        continue

    amount += coin

print(f"Enjoy your coke! Your change is {amount - 50} ")

