# Password Generator Project
import random

# Character sets for password generation
letter_chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
number_chars = list('0123456789')
symbol_chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("Enter the complexity of the password:\n 1. Easy \n 2. Intermediate \n 3. Hard \n")
password_complexity = input().lower()

password_elements = []

if password_complexity == "hard":
    num_letters = int(input("How many letters would you like in your password?\n")) 
    num_symbols = int(input("How many symbols would you like?\n"))
    num_numbers = int(input("How many numbers would you like?\n"))
    total_chars = num_letters + num_symbols + num_numbers

    if total_chars >= 12:
        for _ in range(num_letters):
            password_elements.append(random.choice(letter_chars))
        for _ in range(num_symbols):
            password_elements.append(random.choice(symbol_chars))
        for _ in range(num_numbers):
            password_elements.append(random.choice(number_chars))

        random.shuffle(password_elements)
        final_password = "".join(password_elements)
        print(f"Your password is: {final_password}")

    else:
        print("The total length of the password should be at least 12 characters.")

elif password_complexity == "intermediate":
    num_letters = int(input("How many letters would you like in your password?\n")) 
    num_numbers = int(input("How many numbers would you like?\n"))
    total_chars = num_letters + num_numbers

    if total_chars >= 8:
        for _ in range(num_letters):
            password_elements.append(random.choice(letter_chars))
        for _ in range(num_numbers):
            password_elements.append(random.choice(number_chars))

        random.shuffle(password_elements)
        final_password = "".join(password_elements)
        print(f"Your password is: {final_password}")

    else:
        print("The length should be at least 8 characters.")

elif password_complexity == "easy":
    num_letters = int(input("How many letters would you like in your password?\n")) 
    
    if num_letters >= 5:
        for _ in range(num_letters):
            password_elements.append(random.choice(letter_chars))

        random.shuffle(password_elements)
        final_password = "".join(password_elements)
        print(f"Your password is: {final_password}")

    else:
        print("The length should be at least 5 characters.")

else:
    print("Invalid input.")
