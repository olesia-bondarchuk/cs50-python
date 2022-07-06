def main():
    fruit_name = input("Fruit name: ")
    calories = fruit_calories(fruit_name)
    if calories == -1:
        print("Unknown fruit!!!")
    else:
        print(f"Calories: {calories}")

def fruit_calories(fruit_name):
    calories_table = {"strawberry": 100, "apple": 50, "avocado": 80 }
    fruit_name = fruit_name.lower()

    if fruit_name not in calories_table:
        return -1
    else:
        return calories_table[fruit_name] 

if __name__ == "__main__":
    main()