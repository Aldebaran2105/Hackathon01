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

    allowed_chars = set("0123456789+-*/(). ")
    if not all(char in allowed_chars for char in expression):
        raise ValueError("Carácter inválido en la expresión")

    try:
        tree = ast.parse(expression, mode='eval')
        return _evaluate(tree.body)
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis inválida")
    except Exception:
        raise ValueError("Expresión inválida o no soportada")

def _evaluate(node):
    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](left, right)
        else:
            raise ValueError("Operador no permitido")

    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](operand)
        else:
            raise ValueError("Operador unario no permitido")

    elif isinstance(node, ast.Num):  # Python < 3.8
        return node.n

    elif isinstance(node, ast.Constant):  # Python >= 3.8
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Constante inválida")

    else:
        raise ValueError("Expresión no soportada")