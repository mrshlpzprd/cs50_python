# Take user's input and convert to emoji
def convert(phrase):
    if phrase == 'Hello :)':
        print('Hello 🙂')
    elif phrase == 'Goodbye :(':
        print('Goodbye 🙁')
    elif phrase == 'Hello :) Goodbye :(':
        print('Hello 🙂 Goodbye 🙁')

# Ask user for input and send result to be converted
def main():
    phrase = input("Please say 'Hello :)', 'Goodbye :(' or both to me.\n")
    convert(phrase)

# Print the result
main()
