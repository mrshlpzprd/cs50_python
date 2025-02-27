import sys

# Prompt the user for a vanity plate and Output Valid or Invalid
def main():

    try:
        s = input('Plate: ')
        s = s.upper()
        if is_valid(s):
            print('Valid')
        else:
            print('Invalid')

    except:
        sys.exit(0)

# Check if plate is Valid/ Invalid
def is_valid(s):
    return (
        starts_two_letters(s) and
        plate_length(s) and
        num_at_end(s) and
        first_number_not_zero(s) and
        not_special_characters(s)
    )

# Must start with at least two letters
def starts_two_letters(s):
    sliced_plate = s[0:2]
    sliced_plate = sliced_plate.isalpha()
    return sliced_plate

# Min 2, max 6 char (letters or numbers)
def plate_length(s):
    plate_length = len(s)
    return 2 <= plate_length <= 6

# Numbers must be at the end
def num_at_end(s):
    for char in range(len(s) - 1):
        if s[char].isdigit() and s[char + 1].isalpha():
            return False
    return True

# Can't start with 0
def first_number_not_zero(s):
    for char in s:
        if char.isdigit():
            return char != '0'
    return True

# No periods, spaces, or punctuation marks
def not_special_characters(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
