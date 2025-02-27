# Prompt the user for a vanity plate and Output Valid or Invalid
def main():
    plate = input("Plate: ")
    plate = plate.upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Check if plate is Valid/ Invalid
def is_valid(plate):
    return (
        starts_two_letters(plate) and
        plate_length(plate) and
        num_at_end(plate) and
        first_number_not_zero(plate) and
        not_special_characters(plate)
    )

# Must start with two letters
def starts_two_letters(plate):
    sliced_plate = plate[0:2]
    sliced_plate = sliced_plate.isalpha()
    return(sliced_plate)

# Min 2 char, max 6 char
def plate_length(plate):
    plate_length = len(plate)
    return 2 <= plate_length <= 6

# Numbers must be at the end
def num_at_end(plate):
    for char in range(len(plate) - 1):
        if plate[char].isdigit() and plate[char + 1].isalpha():
            return False
    return True

# Can't start with 0
def first_number_not_zero(plate):
    for char in plate:
        if char.isdigit():
            return char != "0"
    return True

# No periods, spaces, or punctuation marks
def not_special_characters(plate):
    if plate.isalnum():
        return True
    else:
        return False

main()
