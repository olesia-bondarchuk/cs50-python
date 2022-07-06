def main():
    t = int(input("Enter a mass in kg: "))
    t = energy(t)

    print(t)

def energy(mass):
    c = 300000000
    return mass * (c ** 2)

main()