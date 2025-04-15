def calculate(expression: str) -> float:
    expression = expression.strip()

    if not expression:
        raise ValueError("La expresión no puede estar vacía")

    allowed_chars = set("0123456789+-*/(). ")

    if not all(char in allowed_chars for char in expression):
        raise ValueError("Carácter inválido en la expresión")

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis inválida")
    except Exception:
        raise ValueError("Error desconocido")
