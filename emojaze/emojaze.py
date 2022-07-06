from xml.etree.ElementInclude import include


import emoji

def main():

    name = input("Enter a code: ")
    print(f"Output: {emoji.emojize(name, language='alias')}")

if __name__ == "__main__":
    main() 