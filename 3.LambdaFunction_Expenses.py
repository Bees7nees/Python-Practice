'''
  Lambda functions give you a concise way to write small, throwaway functions in your code.
  In this project, we explore the power of Lambda Functions by creating an expense tracker.
  We will demonstrate how you can use Lambda Functions for efficient, streamlined operations.
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
