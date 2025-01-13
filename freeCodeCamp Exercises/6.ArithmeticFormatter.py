def arithmetic_arranger(problems, show_answers=False):
    
    first_line = []
    second_line = []
    dashes_line = []
    results_line = []
    
    if len(problems) > 4:
        return "Error: Too many problems."
    
    for problem in problems:
        parts = problem.split()
        first_digit = parts[0]
        operator = parts[1]
        second_digit = parts[2]
        result = 0
        
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not first_digit.isdigit() or not second_digit.isdigit():
            return "Error: Problems must only contain digits."
        if len(first_digit) > 4 or len(second_digit) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        column_width = max(len(first_digit), len(second_digit)) + 2
        
        first_line.append(first_digit.rjust(column_width))
        second_line.append(operator + " " + second_digit.rjust(column_width - 2))
        dashes_line.append("-" * column_width)
        
        if show_answers:
            result = int(first_digit) + int(second_digit) if operator == "+" else int(first_digit) - int(second_digit)
            results_line.append(str(result).rjust(column_width))
        
    formatted_problems = "    ".join(first_line) + \
                        "    ".join(second_line) + \
                        "    ".join(dashes_line) + \
                        "    ".join(results_line)
        
    print(formatted_problems)
    
                    
    return formatted_problems

print(arithmetic_arranger(["32 + 698", "1 - 2", "45 + 43", "123 + 49", "12 + 3"]))  # Should return the error message
print(arithmetic_arranger(["32 * 698"]))           # Should return the operator error message
print(arithmetic_arranger(["32a + 698"]))            # Should return digit error
print(arithmetic_arranger(["12345 + 12"]))           # Should return length error
arithmetic_arranger(["32 + 8", "1 - 999", "123 + 49", "5 + 6"], True)