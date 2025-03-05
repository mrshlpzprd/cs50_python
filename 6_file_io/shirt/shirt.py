import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not os.path.splitext(sys.argv[1])[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    elif not os.path.splitext(sys.argv[2])[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        try:
            cs50_p_shirt()
        except FileNotFoundError:
            sys.exit("Input does not exist")


def cs50_p_shirt():
    shirt = Image.open("shirt.png")
    size = shirt.size   # Shirt size = (600, 600)

    with Image.open(sys.argv[1]) as muppet:
        muppet = ImageOps.fit(muppet, size)
        muppet.paste(shirt, (0, 0), shirt)
        muppet.save(sys.argv[2])


if __name__ == "__main__":
    main()
