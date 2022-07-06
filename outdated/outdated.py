def parseDate(date: str) -> str:
    result = ""
    
    try:
        result = parseDateInMiddleEndian(date)
    except Exception as e1:
        try:
            result = parseDateInFullFormat(date)
        except Exception as e2:
            raise Exception(f"Unknown format: MiddleEndian: {e1}; Full: {e2}")

    return result

def parseDateInMiddleEndian(user_date: str) -> str:

    date = user_date.split("/")
    if len(date)!= 3:
        raise Exception("Invalid format")
    result = ""

    month = int(date[0])
    if month >= 1 and month <=12:
        result = result + addZero(month) + "-"
    else:
        raise Exception("Invalid month")


    day = int(date[1])
    if day>=1 and day <= 31:
        result = result+ addZero(day)
    else:
        raise Exception("Invalid day")

    year = int(date[2])
    result = str(year) + "-" + result

    return result

def parseDateInFullFormat(user_date: str) -> str:
    months_list = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }

    parts = user_date.split(" ")
    if len(parts) != 3:
        raise Exception("Invalid format")

    year = int(parts[2])
    result = str(year) + "-"

    if parts[0] not in months_list:
        raise Exception("Invalid month")
    
    result += addZero(months_list[parts[0]]) + "-"

    if not parts[1].endswith(","):
        raise Exception("Invalid day format")
    
    day = int(parts[1][:-1])
    if day < 1 or day > 31:
        raise Exception("Invalid day")

    result += addZero(day)

    return result

def addZero(n: int) -> str:
    return f"{n:02}"

if __name__ == "__main__":
    try:
        date = input("Enter the date (MM/DD/YYYY): ")
        result = parseDate(date)

        print(f"Date: {result}")
        exit(0)
    except Exception as e:
        print(f"Error during execution: {e}")
        exit(1)