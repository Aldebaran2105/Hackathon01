from src.main import calculate

def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión no puede estar vacía")

    expression = expression.strip()

    # Validar caracteres permitidos
    for char in expression:
        if not (char.isdigit() or char.isspace() or char in "+-*/()."):
            raise ValueError(f"Carácter inválido encontrado: '{char}'")
        
    try:
        # Evalúa la expresión matemáticamente
        resultado = eval(expression, {"_builtins_": None}, {})
        return resultado
    except ZeroDivisionError:
            raise ZeroDivisionError("División por cero")
    except SyntaxError:
            raise SyntaxError("Sintaxis inválida")
    except Exception:
            raise ValueError("Error desconocido")