import csv
import sys
from typing import Dict, List

def main():
    if len(sys.argv) != 3:
        sys.exit("Wrong number of command line arguments.")
    
    try:
        rewrite_csv_file(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("File is not found.")


def rewrite_csv_file(originalFilePath: str, resultFilePath: str) -> None:
    original_file = open(originalFilePath, "r")
    result_file = open(resultFilePath, "w")

    original_data = csv.DictReader(original_file)
    result_data = process_data(original_data)

    writer = csv.DictWriter(result_file, ["first_name", "last_name", "house"])
    writer.writeheader()
    writer.writerows(result_data)

    original_file.close()
    result_file.close()


def process_data(input: List[Dict[str, str]]) -> List[Dict[str, str]]:
    result = [] 
    for row in input:
        last_name, first_name = row["name"].split(", ")
        new_row = { "first_name": first_name, "last_name": last_name, "house": row["house"] }

        result.append(new_row)
    
    return result

if __name__ == "__main__":
    main()