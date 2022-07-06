import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) != 2:
        sys.exit("Wrong number of commmand line arguments.")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Wrong file exstension.")

    print(tabulated_csv_file(sys.argv[1]))

def tabulated_csv_file(file_path):
    if file_path == None:
        raise ValueError("Argument must not be None.")

    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        sys.exit("File does not exist.")

    reader = csv.DictReader(file)
    return tabulate(reader, tablefmt="grid")

if __name__ == "__main__":
    main()