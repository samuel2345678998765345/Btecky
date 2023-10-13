import string
import random

def generate_password(length):
    # All possible characters that can be included in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use the random.sample function to ensure that the characters are not repeated
    # If repetition is allowed, use random.choices instead
    password = random.sample(all_characters, length)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

# Generate a 12-character password
print(generate_password(12))
