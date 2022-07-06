import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
   return len(re.findall("[^a-zA-Z0-9]?um(?:[^a-zA-Z0-9]|$)", s, re.IGNORECASE))

if __name__ == "__main__":
    main()