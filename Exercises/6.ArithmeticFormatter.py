def arithmetic_arranger(problems, show_answers=False):
    
    # Check if there are more than 5 problems. If so, return an error message.
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Loop through each problem.
    for problem in problems:
        # Split the problem into its parts (e.g. "32 + 698" becomes ["32", "+", "698"]).
        problem = problem.split()
        
        # Check if the operator is not one of the allowed operators.
        if problem[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if the numbers are not numeric.
        if not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Error: Numbers must only contain digits."
        
        # Check if the numbers are more than 4 digits.
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        separator = "-" * (max(len(problem[0]), len(problem[2])) + 2)
        
        # Print the problem.
        
        print(f'{problem[0].rjust(len(separator))}\n{problem[1]}{problem[2].rjust(len(separator))}\n{separator}')
        
        
                       
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')