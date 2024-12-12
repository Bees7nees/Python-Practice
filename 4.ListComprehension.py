'''
I will learn how to construct a new Python list from an iterable types: lists, tuples, and strings, using List Comprehension.
This allows me to create a new list without using a for loop or the `.append()` list method.

In this project, I will write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

The project has two phases: first, I will use a for loop to implement the program.
Then, I will learn how to use List Comprehension instead of a loop to achieve the same results.

Earlier versions of the code are left commented for reference.
'''

def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Converts a string from Camel Case or Pascal Case to Snake Case.

    Parameters:
    pascal_or_camel_cased_string (str): The input string in Camel Case or Pascal Case format.

    Returns:
    str: The converted string in Snake Case format.
    """
    # Create a list of characters, converting uppercase to lowercase
    # and prepending an underscore
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the characters into a string and strip leading underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Test the convert_to_snake_case function with a sample string
    print(convert_to_snake_case('IAmAPascalCasedString'))
    
'''
def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')
    # return clean_snake_cased_string

    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()
'''
'''
def convert_to_snake_case(pascal_or_camel_cased_string):
    
    # This function takes a string formatted in Camel Case or Pascal Case
    # and converts it into Snake Case.

    # It does this by looping through each character in the string and
    # appending it to a list. If the character is an uppercase letter, it
    # is converted to lowercase and an underscore is added before it.

    snake_cased_char_list = [] # Initialize an empty list to store the characters in snake case
    for char in pascal_or_camel_cased_string:
        if char.isupper(): # Check if the character is an uppercase letter
            converted_character = '_' + char.lower() # Convert it to lowercase and add an underscore before it
            snake_cased_char_list.append(converted_character) # Add the converted character to the list
        else:
            snake_cased_char_list.append(char) # If the character is not an uppercase letter, just add it to the list
    snake_cased_string = ''.join(snake_cased_char_list) # Join the characters in the list into a string
'''