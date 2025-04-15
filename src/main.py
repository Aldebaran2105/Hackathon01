def calculate(expression: str) -> float:
    import re
    import operator

    # Definir precedencia y operadores válidos
    ops = {
        '+': (1, operator.add),
        '-': (1, operator.sub),
        '*': (2, operator.mul),
        '/': (2, operator.truediv)
    }

    def parse_tokens(expr):
        token_pattern = re.compile(r"\d+\.\d+|\d+|[-+*/()]")
        return token_pattern.findall(expr)

    def to_rpn(tokens):
        output = []
        stack = []
        for token in tokens:
            if re.fullmatch(r"\d+\.\d+|\d+", token):
                output.append(float(token))
            elif token in ops:
                while stack and stack[-1] in ops and ops[token][0] <= ops[stack[-1]][0]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise SyntaxError("Paréntesis desbalanceados")
                stack.pop()
            else:
                raise ValueError("Carácter inválido en la expresión")
        while stack:
            if stack[-1] in '()':
                raise SyntaxError("Paréntesis desbalanceados")
            output.append(stack.pop())
        return output

    def eval_rpn(rpn):
        stack = []
        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise SyntaxError("Sintaxis inválida")
                b = stack.pop()
                a = stack.pop()
                try:
                    stack.append(ops[token][1](a, b))
                except ZeroDivisionError:
                    raise ZeroDivisionError("División por cero")
        if len(stack) != 1:
            raise SyntaxError("Sintaxis inválida")
        return stack[0]

    expression = expression.strip()
    if not expression:
        raise ValueError("La expresión no puede estar vacía")

    allowed_chars = set("0123456789+-*/(). ")
    if not all(char in allowed_chars for char in expression):
        raise ValueError("Carácter inválido en la expresión")

    tokens = parse_tokens(expression)
    rpn = to_rpn(tokens)
    return eval_rpn(rpn)