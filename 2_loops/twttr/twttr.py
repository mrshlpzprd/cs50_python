# Prompt the user for a str
def main():
    vowel_phrase = input("Input: ")
    remove_vowels(vowel_phrase)

# Check each character
def remove_vowels(vowel_phrase):
    vowels = ["a", "e", "i", "o", "u"]

    for vowel in vowels:
        vowel_phrase = vowel_phrase.replace(vowel, "")
        vowel_phrase = vowel_phrase.replace(vowel.upper(), "")
    print(vowel_phrase)

main()
