def main():
    t = input("Enter text: ")
    t = convert(t)

    print(t)

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()