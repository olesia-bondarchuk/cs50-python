def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = removeprefix(d, "$")
   
    return float(d)


def percent_to_float(p):
    p = removesuffix(p, "%")

    return float(p)/100

def removeprefix(s, p):
    if s[0] == p:
        return s[1:]
    else:
        return s
    
def removesuffix(s, x):
    
    if s[-1] == x:
        return s[:-1]
    else:
        return s

main()