import sys
import requests

def main():
    
    # comment
    if len(sys.argv) != 2:
        sys.exit("Wrong number of command line argumnets!")
   
    n = sys.argv[1]

    if not n.isdigit():
        sys.exit("Command line argument is not a number! ")
    
    try:
        number = float(n)
    except ValueError:
        sys.exit("Wrong command line argument! ")
    
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Fail to get current price")

    result = r.json()

    amount = number * result["bpi"]["USD"]["rate_float"]
    print(f"{amount:,.4f}")
    



if __name__ == "__main__":
    main()