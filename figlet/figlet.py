from pyfiglet import Figlet
import random
import sys


def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Wrong number of arguments")
        sys.exit(127)
    
    
    if len(sys.argv) > 1 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Unknown option")
        sys.exit(128)
    
    fonts = Figlet().getFonts()
    font = ""

    if len(sys.argv) == 3:
        if sys.argv[2] not in fonts:
            print(f"Unknown font '{sys.argv[2]}'")
            print("Available fonts:", fonts)
            sys.exit(129)

        font = sys.argv[2]
    else:
        font = random.choice(fonts)
            

    text = input("Input: ")
    f = Figlet(font = font)
    output = f.renderText(text) 
    
    print(f"Output:\n{output}")

if __name__ == "__main__":
    main()

