class ExpressionEvaluator:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        self.index = 0

    def parse(self):
        if not self.expression:
            raise ValueError("La expresión no puede estar vacía")
        value = self._parse_expression()
        if self.index < len(self.expression):
            raise SyntaxError("Caracteres restantes no válidos")
        return value

    def _parse_expression(self):
        values = [self._parse_term()]
        while self._current() in '+-':
            op = self._consume()
            right = self._parse_term()
            if op == '+':
                values.append(right)
            elif op == '-':
                values.append(-right)
        return sum(values)

    def _parse_term(self):
        values = [self._parse_factor()]
        while self._current() in '*/':
            op = self._consume()
            right = self._parse_factor()
            if op == '*':
                values[-1] *= right
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("División por cero")
                values[-1] /= right
        return values[-1]

    def _parse_factor(self):
        char = self._current()
        if char == '(':
            self._consume()  # consume '('
            value = self._parse_expression()
            if self._consume() != ')':
                raise SyntaxError("Falta el paréntesis de cierre")
            return value
        elif char in '+-':
            op = self._consume()
            factor = self._parse_factor()
            return factor if op == '+' else -factor
        else:
            return self._parse_number()

    def _parse_number(self):
        start = self.index
        while self._current() and self._current().isdigit() or self._current() == '.':
            self.index += 1
        try:
            return float(self.expression[start:self.index])
        except ValueError:
            raise SyntaxError("Número inválido")

    def _current(self):
        return self.expression[self.index] if self.index < len(self.expression) else None

    def _consume(self):
        char = self._current()
        self.index += 1
        return char


def calculate(expression: str) -> float:
    # Validar caracteres
    allowed_chars = set("0123456789+-*/(). ")
    if not expression or not all(char in allowed_chars for char in expression):
        raise ValueError("Expresión vacía o contiene caracteres inválidos")
    evaluator = ExpressionEvaluator(expression)
    return evaluator.parse()
