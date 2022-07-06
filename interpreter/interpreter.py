expression = input("Arithmetic expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

result = 0

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print("{:.1f}".format(result))
