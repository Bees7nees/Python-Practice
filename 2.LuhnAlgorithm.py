'''
The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers.
The Luhn Algorithm is a simple formula for validating a number against a check digit,
usually the last digit of a credit card number. It is a checksum formula that can be
used to validate various identification numbers, such as credit card numbers, National Provider Identifier (NPI) numbers, Canadian Social Insurance Numbers (SINs), etc.
'''

def verify_card_number(card_number):
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

main()
