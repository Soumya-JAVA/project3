#A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create a
#password generator application using Python, allowing users to
#specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the password.
#Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    character_pool = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_numbers, use_special

def main():
    length, use_uppercase, use_numbers, use_special = get_user_input()
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
