def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("La expresión no puede estar vacía")

    expression = expression.strip()
