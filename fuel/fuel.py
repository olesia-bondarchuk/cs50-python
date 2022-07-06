def main():
    
    fuel_amount = input("Fraction (x/y): ")
    
    result = convert(fuel_amount)

    print(gauge(result))
  

def convert(fraction):
    
    result_after_string_split = fraction.split("/")

    if len(result_after_string_split) != 2:
        raise ValueError("Wrong format")
        
    if not result_after_string_split[0].isdigit():
        raise ValueError("First argument should be a number")
      
    if not result_after_string_split[1].isdigit():
        raise ValueError("Second argument should be a number.")
        
    x = int(result_after_string_split[0])
    y = int(result_after_string_split[1])

    if y == 0:
        raise ZeroDivisionError("Second number cannot be 0.")

    if x > y:
        raise ValueError("First number is greater then second one.")

    return round(x/y * 100)


def gauge(percentage):
   
    if percentage < 0 or percentage > 100:
        raise ValueError("Persentage cannot be less than 0 or greater than 100.")

    if percentage<=1:
        return("E")
    elif percentage >=99:
        return("F")
    else:
        return(f"{percentage}%")
    

if __name__ == "__main__":
    main() 