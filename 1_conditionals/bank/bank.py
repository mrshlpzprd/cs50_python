# Prompt user for greeting
greeting = input("Greeting: ")
greeting = greeting.strip().lower()

# Hello $0.00
if greeting.startswith("hello"):
    print("$0")

# Greeting starting with "h" $20.00
elif greeting.startswith("h"):
    print("$20")

# Otherwise output $100.00
else:
    print("$100")
