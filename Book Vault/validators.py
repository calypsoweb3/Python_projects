def integer_validator(prompt, minimum = 1, maximum = 1000):
    while True:
        try:
            valid = int(input(prompt))
            if valid >= minimum and valid <= maximum:
                return valid
            else:
                print(f'Number out of range {minimum} and {maximum}')
        except ValueError:
            print('Enter a valid integer')
def string_validator(prompt):
    while True:
            abc = input(prompt).strip()
            if not abc:
                print('This field cannot be empty')
                continue
            if not all(char.isalpha() or char.isspace() for char in abc):
                print('Names should contain only letters and spaces.')
                continue
            return abc