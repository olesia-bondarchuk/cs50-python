import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    matches = re.search("^([0-9]|1[0-2])(?:\:)?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(?:\:)?([0-5][0-9])? (AM|PM)$", s)
    
    if not matches:
        raise ValueError("Invalid time.")
    
    time_from = twelve_to_twenty_four_format(matches.group(1), matches.group(2), matches.group(3))
    time_to = twelve_to_twenty_four_format(matches.group(4), matches.group(5), matches.group(6))

    return time_from + " to " + time_to

def twelve_to_twenty_four_format(hours, minutes, am_pm):
    hours = int(hours)
    
    if minutes == None or minutes == "":
        minutes = "0"
   
    minutes = int(minutes)

    if hours > 12 or minutes >= 60:
        raise ValueError("Invalid time.")

    if am_pm == "PM":
        hours += 12
    
    return f"{hours}:{minutes:02}" 
    
        

if __name__ == "__main__":
    main()
