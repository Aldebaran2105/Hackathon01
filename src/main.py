def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión no puede estar vacía")

    expression = expression.strip()

    # Validar caracteres permitidos
    for char in expression:
        if not (char.isdigit() or char.isspace() or char in "+-*/()."):
            raise ValueError(f"Carácter inválido encontrado: '{char}'")