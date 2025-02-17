# A Python module is a file that contains a set of statements and definitions
# that you can use in your code.

# In this project, we learn how to import modules from the Python standard
# library. We also learn how to use Regular Expressions by building your
# own password generator program.

# import random
import re
import secrets
import string

# It is common practice to place import statements at the top of your code file.
# Additionally, when there are multiple import statements, sorting them in alphabetical
# order can improve readability.

# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)

# Every time the code runs, you should see a random character from the all_characters string.
# This is exactly what you want to achieve to create a random password.

# However, the algorithm on which random relies makes the generated pseudo-random numbers predictable.
# Therefore, although the random module is suitable for the most common applications, it cannot be
# used for cryptographic purposes, due to its deterministic nature.

# Instead of importing random, import the secrets module. Then change the print() call to
# use secrets.choice(all_characters).

# print(random.choice(all_characters))


def generate_password(length):
    # Define the possible characters for the password
    
    # string.ascii_letters: A string containing all ASCII letters (both lowercase and uppercase)
    letters = string.ascii_letters

    # string.digits: A string containing all decimal digits ('0' to '9')
    digits = string.digits

    # string.punctuation: A string containing all ASCII punctuation characters
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    '''
    password = ''
    # Generate password
        # A standalone single underscore is used to represent a value you don't care
        # about or that won't be used in your code. In this case, instead of i we can use _
    for _ in range(length):
        password += secrets.choice(all_characters)
    '''
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        # A tuple is another built-in data structure in Python.
        # Tuples are very much like lists, but they are defined with
        # parentheses (), instead of square brackets.
        # Also, tuples are immutable, unlike lists.

        # Constraints for the generated password
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),            
            (special_chars, fr'[{symbols}]')            
        ]

        # Check constraints
        '''
        Instead of using a loop and a counter variable, I'm going to achieve the same result with a different approach in the next few steps.
        
        I'll start by initializing the counter variable to 0.
        Then, I'll use a for loop to iterate over the constraints list.
        For each constraint, I'll use the re.findall() method to find all matches of the pattern in the password.
        If the length of the matches is greater than or equal to the constraint, I'll increment the counter.
        Finally, if the counter is equal to the length of the constraints list, I'll break out of the loop and return the password.
        '''
        # Check each constraint to ensure that the generated password meets the requirements
        # by counting the number of matches of the pattern in the password.
        # If the length of the matches is greater than or equal to the constraint,
        # then the constraint is satisfied.
        # If all constraints are satisfied, break out of the loop and return the password.
        if all(
            # For each constraint, count the number of matches of the pattern in the password
            # and check if it is greater than or equal to the constraint
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    # Return the generated password
    return password
    
    # This is a special variable in Python that is set to the string "__main__"
    # when the script is run directly (not imported). Therefore, this block of
    # code will only be executed when the script is run directly, not when it
    # is imported as a module. This is a common pattern in Python to add code
    # that should only be executed when the script is run directly.
if __name__ == '__main__':
    # Call the generate_password function to create a new password
    new_password = generate_password()
    # Print the generated password
    print('Generated password:', new_password)


# A regular expression, or regex, is a pattern used to match a specific combination
# of characters inside a string.

# It is a valid alternative to if/else conditional statements when you need to match
# or find patterns inside a string for validation purposes, character replacement,
# and others.

# The compile() function from the re module compiles the string passed as the
# argument into a regular expression object that can be used by other re methods.
