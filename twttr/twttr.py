from sqlalchemy import null


def main():

    s = input("Input: ")
   
    print(f"Output: {shorten(s)}")


def shorten(word):
    if word == None or word == "":
        raise ValueError("Input cannot be null or empty")
    output = ""
    for c in word:
        c2 = c.lower()
        if c2 != "a" and c2 != "e" and c2 != "i" and c2 != "u" and c2 != "o":
            output += c
    
    if output == "":
        raise ValueError("Result cannot be empty.")

    return output



if __name__ == "__main__":
    main()
