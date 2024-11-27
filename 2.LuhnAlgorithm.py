'''
The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers.
The Luhn Algorithm is a simple formula for validating a number against a check digit,
usually the last digit of a credit card number. It is a checksum formula that can be
used to validate various identification numbers, such as credit card numbers, National Provider Identifier (NPI) numbers, Canadian Social Insurance Numbers (SINs), etc.
'''

def verify_card_number(card_number):
    '''
    Verifies a given card number against the Luhn Algorithm checksum.
    '''
    print(f'Verifying card number {card_number}')
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    print(odd_digits)

def main():
    '''
    Main function.
    '''
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(f'Translated card number: {translated_card_number}')

    verify_card_number(translated_card_number)


main()

