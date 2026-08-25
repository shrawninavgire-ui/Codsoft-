import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask the user for password length
length = int(input("Enter the desired password length: "))

if length <= 0:
    print("Please enter a valid password length.")
else:
    # Characters used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the password
    print("\nGenerated Password:", password)
