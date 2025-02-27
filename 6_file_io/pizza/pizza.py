import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            pizza_rows = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pizza_rows.append(row)
            print(tabulate(pizza_rows, headers="keys", tablefmt="grid"))
        except FileNotFoundError as file:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
