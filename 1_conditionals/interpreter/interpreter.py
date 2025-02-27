# Prompt user for arithmetic expression
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

# Calculate arithmetic expression and output result as floating point (one decimal place)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
else:
    print(float(x / z))

