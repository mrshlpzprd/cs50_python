import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        qty_lines = 0
        with open(sys.argv[1], "r") as file:
            all_lines = file.readlines()
            for line in all_lines:
                line = line.lstrip()
                if not (line == "" or line.startswith("#")):
                    qty_lines += 1
        print(qty_lines)
    except FileNotFoundError as file:
        print("File does not exist")
