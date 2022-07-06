def main():

    grocery_list = {}
    while True:
        try:
            item = input("").lower()
            if item not in grocery_list:
                grocery_list[item] = 0
            grocery_list[item] += 1  
        except EOFError:
            break
    
    print("     ")

    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == "__main__":
    main() 