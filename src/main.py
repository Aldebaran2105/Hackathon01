import re

def calculate(expression: str) -> float:
    expression = expression.strip()
    if not expression:
        raise ValueError("La expresión no puede estar vacía")

    allowed_chars = set("0123456789+-*/(). ")
    if not all(char in allowed_chars for char in expression):
        raise ValueError("Carácter inválido en la expresión")

    try:
        tokens = tokenize(expression)
        rpn = to_rpn(tokens)
        return evaluate_rpn(rpn)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis inválida")
    except Exception:
        raise ValueError("Error desconocido")

def tokenize(expression: str):
    token_pattern = r'\d+\.\d+|\d+|[+\-*/()]'
    tokens = re.findall(token_pattern, expression.replace(' ', ''))

    # Manejar números negativos (unarios)
    processed = []
    prev = None
    for token in tokens:
        if token == '-' and (prev is None or prev in "+-*/("):
            processed.append('0')  # Ej: -5 -> 0 - 5
        processed.append(token)
        prev = token
    return processed

def to_rpn(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise SyntaxError("Paréntesis no balanceados")
            stack.pop()
        else:
            raise ValueError("Token inválido")

    while stack:
        if stack[-1] in "()":
            raise SyntaxError("Paréntesis no balanceados")
        output.append(stack.pop())

    return output

def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if is_number(token):
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise SyntaxError("Faltan operandos")
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError
                stack.append(a / b)
    if len(stack) != 1:
        raise SyntaxError("Expresión malformada")
    return stack[0]

def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False