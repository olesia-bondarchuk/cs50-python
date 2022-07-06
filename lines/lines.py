import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Wrong number of command line arguments.")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Wrong file extension.")

    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist.")

    code = file.read()
    print(f"Number of lines in {sys.argv[1]}: {count_code_lines(code)}")
    
def count_code_lines(code: str) -> int:

    if code == None:
        raise ValueError("Argument must not be None.")

    line_count = 0

    lines = code.split("\n")
    for line in lines:
        stripped_line = line.lstrip()
        if not (stripped_line.startswith("#") or stripped_line == ""):
            line_count += 1

    return line_count

if __name__ == "__main__":
    main()