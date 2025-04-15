import ast
import operator

# Operadores permitidos
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def calculate(expression: str) -> float:
    expression = expression.strip()

    if not expression:
        raise ValueError("La expresión no puede estar vacía")

    # Validar caracteres permitidos
    if not all(char in "0123456789+-*/(). " for char in expression):
        raise ValueError("Carácter inválido en la expresión")

    try:
        tree = ast.parse(expression, mode='eval')
        return _evaluate(tree.body)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis inválida")
    except Exception as e:
        raise ValueError(f"Expresión inválida o no soportada: {e}")


def _evaluate(node):
    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise ValueError("Operador no permitido")
        return OPERATORS[op_type](left, right)

    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise ValueError("Operador unario no permitido")
        return OPERATORS[op_type](operand)

    elif isinstance(node, (ast.Num, ast.Constant)):  # Soporte para 3.11 y 3.12
        value = getattr(node, 'n', getattr(node, 'value', None))
        if isinstance(value, (int, float)):
            return value
        else:
            raise ValueError("Constante inválida")

    raise ValueError("Expresión no soportada")
