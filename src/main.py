def calculate(expression: str) -> float:





    # Validar caracteres permitidos
    for char in expression:
        if not (char.isdigit() or char.isspace() or char in "+-*/()."):
            raise ValueError(f"Carácter inválido encontrado: '{char}'")
