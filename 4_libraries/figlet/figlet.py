import random, sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    my_font = random.choice(figlet.getFonts())
    figlet.setFont(font=my_font)

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        my_font = sys.argv[2]
        figlet.setFont(font=my_font)
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

if my_font in figlet.getFonts():
    my_input = input("Input: ")
    print(figlet.renderText(my_input))
else:
    sys.exit("Invalid usage")
