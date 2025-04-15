def calculate(expression: str) -> float:

    expression = expression.strip()
    # Casos especiales
    if not expression:
        raise ValueError("Expresión vacía")
    if expression.lower() == 'c':
        return 0.0
    
    # Validación de caracteres
    if not _is_valid_expression(expression):
        raise ValueError("Caracteres no válidos")
    
    # Tokenización y evaluación
    tokens = _tokenize(expression)
    return _evaluate(tokens)

def _is_valid_expression(expr: str) -> bool:
    """Valida caracteres permitidos: números, operadores, espacios y paréntesis"""
    allowed_chars = set("0123456789.+-*/() ")
    return all(c in allowed_chars for c in expr)

def _tokenize(expr: str) -> list:
    """Convierte la expresión en tokens (números, operadores, paréntesis)"""
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
        elif expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        elif expr[i].isdigit() or expr[i] == '.':
            num = ""
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(float(num))
        else:
            raise ValueError(f"Carácter inválido: '{expr[i]}'")
    return tokens

def _evaluate(tokens: list) -> float:
    """Evalúa tokens con precedencia y paréntesis"""
    # Primero evalúa paréntesis
    while '(' in tokens:
        idx_open = tokens.index('(')
        idx_close = _find_matching_parenthesis(tokens, idx_open)
        tokens[idx_open:idx_close+1] = [_evaluate(tokens[idx_open+1:idx_close])]
    
    # Luego multiplicaciones y divisiones
    i = 1
    while i < len(tokens):
        if tokens[i] == '*':
            tokens[i-1] *= tokens[i+1]
            del tokens[i:i+2]
        elif tokens[i] == '/':
            if tokens[i+1] == 0:
                raise ZeroDivisionError("División por cero")
            tokens[i-1] /= tokens[i+1]
            del tokens[i:i+2]
        else:
            i += 1
    
    # Finalmente sumas y restas
    result = tokens[0] if tokens else 0.0
    i = 1
    while i < len(tokens):
        if tokens[i] == '+':
            result += tokens[i+1]
            i += 2
        elif tokens[i] == '-':
            result -= tokens[i+1]
            i += 2
        else:
            raise ValueError(f"Operador no soportado: '{tokens[i]}'")
    return result

def _find_matching_parenthesis(tokens: list, idx_open: int) -> int:
    """Encuentra el paréntesis de cierre correspondiente"""
    level = 1
    for i in range(idx_open + 1, len(tokens)):
        if tokens[i] == '(':
            level += 1
        elif tokens[i] == ')':
            level -= 1
            if level == 0:
                return i
    raise SyntaxError("Paréntesis no balanceados")