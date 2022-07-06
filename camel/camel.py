camel_case = input("camelCase: ")
snake_case = ""

for c in camel_case: # for each c in array ['h', 'e', 'l', 'l', '0'] do following
    if c.isupper():
        c = c.lower()
        if snake_case != "":
            snake_case += "_"
    
    snake_case += c
    
        
print("snake_case: ", snake_case)
   
for i in range(len(camel_case)): # for i in [0,1,2,3,4] # camel_case = 'hello'
    print(f"s[{i}] = '{camel_case[i]}'")