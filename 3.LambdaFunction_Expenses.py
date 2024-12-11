'''
  Lambda functions give you a concise way to write small, throwaway functions in your code.
  In this project, we explore the power of Lambda Functions by creating an expense tracker.
  We will demonstrate how you can use Lambda Functions for efficient, streamlined operations.
  
  In this file I have saved earlier versions of the code, and are left commented for reference.
'''

def add_expense(expenses, amount, category):
    """
    Adds a new expense to the given list of expenses.
    
    Parameters:
    expenses (list): The list of expenses to add the new expense to.
    amount (float): The amount of the expense.
    category (str): The category of the expense.
    """
    expenses.append({'amount': amount, 'category': category})
    print(f'Added expense: Amount: {amount}, Category: {category}')
    
def print_expenses(expenses):
    """
    Prints out all the expenses in the given list of expenses.
    
    Parameters:
    expenses (list): The list of expenses to print.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calculates the total amount of all expenses in the given list of expenses.
    
    Parameters:
    expenses (list): The list of expenses to calculate the total of.
    """
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filters the given list of expenses by the given category.
    
    Parameters:
    expenses (list): The list of expenses to filter.
    category (str): The category to filter the expenses by.
    """
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    """
    The main function of the program.
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()


'''
# The add_expense function takes in a list of expenses and adds a new one
# It takes in the amount and category of the expense
# It appends a dictionary to the expenses list with the amount and category
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    print(f'Added expense: Amount: {amount}, Category: {category}')
    
# The print_expenses function takes in a list of expenses and prints them out
# It loops through each expense and prints out the amount and category
def print_expenses(expenses):
    print('Expenses:')
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# The total_expenses function takes in a list of expenses and returns the total amount of all expenses
# It uses the map() function to apply a lambda function to each expense in the list
# The lambda function takes in an expense and returns the amount of that expense
# The sum() function is then used to add up all the amounts
def total_expenses(expenses):
    total = sum(map(lambda expense: expense['amount'], expenses))
    print(f'Total: {total}')
    return total
    
# Initialize an empty list to store our expenses
expenses = []
'''
'''
  # In python, we create lists using square brackets
  # Lists are mutable
  # Lists are ordered
  # Lists are indexed

  # Let's create a list
  
  my_list = [1, 2]

  my_list.append(3)
  print(my_list)

  print(my_list[0])

  my_list[0] = 0
  print(my_list)

  my_list.insert(1, 1)
  print(my_list)

  my_list.pop()
  print(my_list)
'''
'''
# The add_expense function takes in a list of expenses and adds a new one
# It takes in the amount and category of the expense
# It appends a dictionary to the expenses list with the amount and category
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
# The print_expenses function takes in a list of expenses and prints them out
# It loops through each expense and prints out the amount and category
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


# Initialize an empty list to store our expenses
expenses = []

# Lambda functions are brief, anonymous functions in Python, ideal for
# simple, one-time tasks. They are defined by the lambda keyword, and
# they use the following syntax
'''

'''
test = lambda x: x * 2
print(list(map(test, [2,3,5,8])))
This code block shows how to use a lambda function to double each number in a given list
The lambda function takes in one argument, x, and returns x * 2
The map() function applies this lambda function to each element in the given list
The list() function is used to convert the result into a list
'''