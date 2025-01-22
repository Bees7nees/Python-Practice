def arithmetic_arranger(problems, show_answers = False):
    
    first_line = []
    second_line = []
    dash_line = []
    results_line = []
    problem_spacing = "    "
    arranged_problems = []
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        parts = problem.split()
        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]
        answer = int
        
        if operator not in ["-", "+"]:
            return "Error: Operator must be '+' or '-'."
        
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        column_width = max(len(first_number), len(second_number)) + 2
        
        dash_line.append("-" * column_width)
        
        first_line.append(first_number.rjust(column_width))
        
        second_line.append(operator + second_number.rjust(column_width - 1))
                    
        if show_answers:
            
            if operator == "-":
                answer = int(first_number) - int(second_number)
                results_line.append(str(answer).rjust(column_width))
            
            else:
                answer = int(first_number) + int(second_number)
                results_line.append(str(answer).rjust(column_width))
            
    first_line = problem_spacing.join(first_line)
    second_line = problem_spacing.join(second_line)
    dash_line = problem_spacing.join(dash_line)
    results_line = problem_spacing.join(results_line)
    
    if show_answers:
        arranged_problems = [first_line, second_line, dash_line, results_line]
        arranged_problems = "\n".join(arranged_problems)
        print(arranged_problems)
    
    else:
        arranged_problems = [first_line, second_line, dash_line]
        arranged_problems = "\n".join(arranged_problems)
        print(arranged_problems)
    
    return arranged_problems
# print(arithmetic_arranger(["32 + 698", "1 - 2", "45 + 43", "123 + 49", "12 + 3", "12 + 3"])) # Should return the error message too many problems
# print(arithmetic_arranger(["32 * 698"])) # Should return the operator error message
# print(arithmetic_arranger(["32a + 698"])) # Should return digit error
# print(arithmetic_arranger(["12345 + 12"]))  # Should return length error
arithmetic_arranger(["3801 - 2", "123 + 49"], False) #should return   3801      123\n-    2    +  49\n------    -----
arithmetic_arranger(["1 + 2", "1 - 9380"]) #should return   1         1\n+ 2    - 9380\n---    ------.
arithmetic_arranger(["3 + 855", "988 + 40"], True) #should return     3      988\n+ 855    +  40\n-----    -----\n  858     1028.
