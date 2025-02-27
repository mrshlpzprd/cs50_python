import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            with open(sys.argv[1], "r") as before, open(sys.argv[2], "w", newline="") as after:
                reader = csv.DictReader(before)
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    name, house = row["name"], row["house"]       # "house": house
                    split_name = name.split(", ")
                    first, last = split_name[1], split_name[0]       # "first": first, "last": last
                    writer.writerow({"first": first, "last": last, "house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
