
groceries = {}

def main():
    while True:
        try:
            grocery = input("").lower()

            if grocery in groceries:
                groceries[grocery] += 1
            else:
                groceries[grocery] = 1
        except EOFError:
            for key, value in sorted(groceries.items()):
                print(value, key.upper())
            break

main()
