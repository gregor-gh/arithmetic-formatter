def spacer(digit, length, operand=" ", space=" "):

    # define empty line
    line = ""

    # add either operand or space
    line += operand

    # calc number of spaces
    spaces = length - len(digit)

    # add spaces, this will be skipped if spaces is zero
    while spaces > 0:
        line += space
        spaces -= 1

    # once done add number
    line += digit

    # finally add four spaces
    line += "    "

    return line

###############################################################


def arithmetic_arranger(problems, showanswer=False):

    # first test for too many problems passed
    if len(problems) > 5:
        return "Error: Too many problems."

    # split input into left, operand, right
    problemsarray = []
    for problem in problems:
        problemsarray.append(problem.split())

    # lines vars
    firstline = ""
    secondline = ""
    breakline = ""
    answerline = ""

    # check all inputs are valid
    for problem in problemsarray:
        if len(problem) > 3:
            return "Error: Not a valid sum."

        left = problem[0]
        operand = problem[1]
        right = problem[2]

        if operand != "+" and operand != "-":
            return "Error: Operator must be '+' or '-'."
        elif len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            int(left)
            int(right)
        except:
            return "Error: Numbers must only contain digits."

        # check which is larger out of the two values and set length
        if (len(left) > len(right)):
            length = len(left)
        else:
            length = len(right)

        # add one for the blank space
        length += 1

        # call the spacer helper for both lines
        firstline += spacer(left, length)
        secondline += spacer(right, length, operand)

        # use spacer help to add dashes too
        breakline += spacer("", length, "-", "-")

        # if the showanswer flag is true then we also need to calc answer
        if showanswer == True:

            # add or subtract depending on operand
            if operand == "+":
                answer = int(left) + int(right)
            else:
                answer = int(left) - int(right)

            answerline += spacer(str(answer), length)

    # once we're done trim the spaces and concat
    arranged_problems = firstline.rstrip() + "\n" + secondline.rstrip() + \
        "\n" + breakline.rstrip()

    # if show then add that too
    if showanswer:
        arranged_problems += "\n"+answerline.rstrip()

    return arranged_problems


print(arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
