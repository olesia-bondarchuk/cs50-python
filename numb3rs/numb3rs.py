import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:

    number_pattern = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

    match = re.search(f"^{number_pattern}\.{number_pattern}\.{number_pattern}\.{number_pattern}$", ip)

    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()