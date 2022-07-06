import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    match = re.search("src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\"", s, re.IGNORECASE)

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()