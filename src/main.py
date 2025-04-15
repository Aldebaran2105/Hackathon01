import re

def calculate(expression):
    expression = expression.strip()

    if not expression:
        raise ValueError("Imput invalido")
    #Check
    if not re.match(r'^[\d\s\+\-\*/\(\)\.]+$', expression):
        raise ValueError("Caracter invalido en la expresion")
    try:
        #Evaluar expresion
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("No se permite dividir por cero")
    except SyntaxError:
        raise SyntaxError("Sintaxis invalidad en la expresion")
    except Exception as e:
        raise ValueError(f"Ha ocurrido un error: {str(e)}")
#Ejemplo:
if _name_ == "_main_":
    print(calculate("4 / 2"))