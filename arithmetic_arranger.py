def arithmetic_arranger(problems, answer=False):
    
    # check to see if the list is too long
    num_problems = len(problems)
    
    answers_list = []
    top_operand = []
    operator = []
    bottom_operand = []

    # calculate answers, create a list of answers
    # check to see if there are too many problems
    if num_problems > 5:
        return "Error: Too many problems."
    for problem in problems:
        problem_list = problem.split()
        # if too many problems, return error
        if (len(problem_list[0]) > 4) or (len(problem_list[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        # try/except to look for ValueErrors
        try:
            if problem_list[1] == '+':
                result = int(problem_list[0]) + int(problem_list[2])
            elif problem_list[1] == '-':
                result = int(problem_list[0]) - int(problem_list[2])
            # return error if wrong operator
            else:
                return "Error: Operator must be '+' or '-'."
        except ValueError: 
            return "Error: Numbers must only contain digits."
        answers_list.append(str(result))

        top_operand.append(problem_list[0])
        operator.append(problem_list[1])
        bottom_operand.append(problem_list[2])
    
    # determine lengths
    # get lengths of all operands, append to list, then determine which to use for spacing purposes
    top_lengths = []
    bottom_lengths = []
    actual_lengths = []

    for value in top_operand:
        top_lengths.append(len(value))

    for value in bottom_operand:
        bottom_lengths.append(len(value))

    # determine which to use for spacing purposes
    for i in range(0, len(top_lengths)):
        if top_lengths[i] >= bottom_lengths[i]:
            actual_lengths.append(top_lengths[i])
        else:
            actual_lengths.append(bottom_lengths[i])
        
        actual_length_int = (int(actual_lengths[i]) + 2) # is for space/operator
        actual_lengths[i] = actual_length_int
    
    # build string

    arranged_problems = ""

    # top row
    i = 0
    for value in top_lengths:
        space_length = actual_lengths[i] - value
        spacing = " " * space_length
        arranged_problems = arranged_problems + spacing
        arranged_problems = arranged_problems + top_operand[i]
        arranged_problems = arranged_problems + "    "
        i += 1
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n" 

    # bottom operands and operators
    i = 0
    for value in bottom_lengths:
        arranged_problems = arranged_problems + operator[i] + " "
        space_length = (actual_lengths[i] - 2) - value
        if space_length > 0:
            spacing = " " * space_length
            arranged_problems = arranged_problems + spacing
        arranged_problems = arranged_problems + bottom_operand[i]
        arranged_problems = arranged_problems + "    "
        i += 1
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    # dashes
    i = 0
    for value in actual_lengths:
        arranged_problems = arranged_problems + ("-" * actual_lengths[i])
        arranged_problems = arranged_problems + "    "
        i += 1
    arranged_problems = arranged_problems.rstrip()

    if answer is True:
        arranged_problems = arranged_problems + "\n"
        i = 0
        for answer in answers_list:
            space_length = actual_lengths[i] - len(answer)
            arranged_problems = arranged_problems + (" " * space_length)
            arranged_problems = arranged_problems + answer
            arranged_problems = arranged_problems + "    "
            i += 1
        arranged_problems = arranged_problems.rstrip()
    
    return arranged_problems