# Ask question to user
deep = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
deep = deep.strip().lower()

# Match for options
match deep:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
