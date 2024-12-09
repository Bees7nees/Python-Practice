'''
The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers.
The Luhn Algorithm is a simple formula for validating a number against a check digit,
usually the last digit of a credit card number. It is a checksum formula that can be
used to validate various identification numbers, such as credit card numbers, National Provider Identifier (NPI) numbers, Canadian Social Insurance Numbers (SINs), etc.
'''

""" def verify_card_number(card_number):
    '''
    Verifies a credit card number using the Luhn Algorithm.
    
    Parameters:
    card_number (str): The credit card number to verify, as a string of digits.
    '''
    sum_of_odd_digits = 0
    
    # Reverse the card number to process from the rightmost digit
    card_number_reversed = card_number[::-1]
    
    # Extract the odd-positioned digits (1-indexed)
    odd_digits = card_number_reversed[::2]

    # Debug output of intermediary steps
    print(f'card_number: {card_number}')
    print(f'card_number_reversed: {card_number_reversed}')
    print(f'odd_digits: {odd_digits}')

    # Sum the odd-positioned digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            print(number)
            number = number // 10 + number % 10

def main():
    '''Main function.'''
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(f'Translated card number: {translated_card_number}')

    verify_card_number(translated_card_number)

main() """

def verify_card_number(card_number):
    """
    Verifies a credit card number using the Luhn Algorithm.

    Parameters:
    card_number (str): The credit card number to verify, as a string of digits.

    Returns:
    bool: True if the card number is valid according to the Luhn Algorithm, False otherwise.
    """
    # Reverse the card number to process from the rightmost digit
    card_number_reversed = card_number[::-1]
    print(f"Reversed card number: {card_number_reversed}")

    # Sum the odd-positioned digits
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    print(f"Odd-positioned digits: {odd_digits}")

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(f"Sum of odd-positioned digits: {sum_of_odd_digits}")

    # Sum the even-positioned digits after multiplying them by 2
    # and subtracting 9 if the result is 10 or greater
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    print(f"Even-positioned digits: {even_digits}")

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    print(f"Sum of even-positioned digits: {sum_of_even_digits}")

    # Check whether the total sum is divisible by 10
    total = sum_of_odd_digits + sum_of_even_digits
    print(f"Total sum: {total}")
    return total % 10 == 0

def main():
    """
    Main function that verifies the validity of a credit card number using the Luhn Algorithm.

    Steps:
    1. Define the credit card number, which may include spaces or dashes.
    2. Remove any spaces or dashes from the credit card number.
    3. Use the verify_card_number function to check if the processed card number is valid.
    4. Print 'VALID!' if the card number is valid, otherwise print 'INVALID!'.
    """
    card_number = '4111-1111-4555-1142'
    print(f"Original card number: {card_number}")
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(f"Translated card number: {translated_card_number}")

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
