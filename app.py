import re

def validate_expression(expr):

    # Remove spaces
    expr = expr.replace(" ", "")

    # Check for invalid characters
    if re.search(r'[^0-9+\-*/^().]', expr):
        return False, "Expression contains invalid characters"

    # Check for balanced parentheses
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False, "Mismatched parentheses"
            stack.pop()
    if stack:
        return False, "Mismatched parentheses"

    # Check for consecutive operators (except unary minus)
    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/^()]', expr)
    prev = None
    for t in tokens:
        if t in '+*/^' and prev in '+-*/^':
            return False, f"Consecutive operators: {prev}{t}"
        prev = t

    # Check expression doesn't start or end with invalid operator
    if tokens[0] in '+*/^':
        return False, "Expression cannot start with operator"
    if tokens[-1] in '+-*/^':
        return False, "Expression cannot end with operator"

    return True, ""

def tokenize(expr):

    expr = expr.replace(" ", "")  # remove spaces

    # Pattern matches numbers (integers or decimals), operators, parentheses
    pattern = r'\d+\.\d+|\d+|[+\-*/^()]'
    raw_tokens = re.findall(pattern, expr)

    tokens = []
    i = 0
    while i < len(raw_tokens):
        t = raw_tokens[i]

        # Check for unary minus: '-' at start or after '(' or operator
        if t == '-' and (i == 0 or raw_tokens[i-1] in '+-*/^('):
            # Combine '-' with next number
            if i + 1 < len(raw_tokens) and re.match(r'\d+\.\d+|\d+', raw_tokens[i+1]):
                tokens.append(str(-float(raw_tokens[i+1])))
                i += 2
                continue
            else:
                # Just a '-' before something else (like '('), keep it
                tokens.append(t)
        else:
            tokens.append(t)
        i += 1

    return tokens

def shunning_yard(expr):

    precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(' : -1}
    operators = ['+', '-', '*', '/', '^', '(', ')']
    output = []
    stack = []
    for token in expr:

        if token not in operators:
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and precedence[token] <= precedence[stack[-1]] and token != '^'):
                output.append(stack.pop())

            stack.append(token)

        
    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(rpn):

    i = 0
    while len(rpn) > 1:
        if rpn[i] not in ['+', '-', '*', '/', '^']:
            i += 1
        else:
            a = float(rpn[i - 2])
            b = float(rpn[i - 1])
            if rpn[i] == '+':
                rpn[i] = a + b
                rpn.pop(i - 1)
                rpn.pop(i - 2)

            elif rpn[i] == '-':
                rpn[i] = a - b
                rpn.pop(i - 1)
                rpn.pop(i - 2)

            elif rpn[i] == '*':
                rpn[i] = a * b
                rpn.pop(i - 1)
                rpn.pop(i - 2)

            elif rpn[i] == '/':
                rpn[i] = a / b
                rpn.pop(i - 1)
                rpn.pop(i - 2)

            elif rpn[i] == '^':
                rpn[i] = a ** b
                rpn.pop(i - 1)
                rpn.pop(i - 2)
            i -= 2

    return rpn[0]

def main():
    expr = input("Enter an expression: ")
    valid, error = validate_expression(expr)
    if not valid:
        print(error)
    else:
        tokens = tokenize(expr)
        rpn = shunning_yard(tokens)
        result = evaluate_rpn(rpn)
        print(f"Result: {result}")

if __name__ == "__main__":
    while True:
        main()