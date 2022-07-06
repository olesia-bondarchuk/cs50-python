import sys

def main():

    name_list = []
    
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    
    l = len(name_list)
    output = "Adieu, adieu, to "

    if l == 0:
        print("No name was provided")
        sys.exit(1)
    
    if l == 1:
        output += name_list[0]
    elif l == 2:
        output += name_list[0] + " and " + name_list[1]
    else:
        for i in range(l-1):
            output += name_list[i] + ", "
        output += "and " + name_list[-1]
    print(f"\nOutput: {output}")


if __name__== __name__:
    main()