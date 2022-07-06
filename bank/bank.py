def main():
   
    greeting = input("Say your greeting: ").lower().strip()
    output = value(greeting)

    print(f"${output}")

def value(greeting):
    
    if greeting == None or greeting == "":
        raise ValueError("Input cannot be null or empty")

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
    

if __name__ == "__main__":
    main()