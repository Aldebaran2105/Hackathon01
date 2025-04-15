# main.py

def suma(a: float, b: float) -> float:
    return a + b

def resta(a: float, b: float) -> float:
    return a - b

def multiplicacion(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

def calculate() -> float:
    while True:
        entrada = input("Ingresa una operación (o 'c' para limpiar): ").strip()

        if entrada.lower() == 'c':
            print("Operación borrada.")
            continue

        # Intentamos parsear operaciones del tipo: número operador número
        try:
            partes = entrada.split()

            if len(partes) != 3:
                raise ValueError("Formato inválido. Usa: número operador número (ej. 2 + 2)")

            a, op, b = partes
            a = float(a)
            b = float(b)

            if op == '+':
                resultado = suma(a, b)
            elif op == '-':
                resultado = resta(a, b)
            elif op == '*':
                resultado = multiplicacion(a, b)
            elif op == '/':
                resultado = division(a, b)
            else:
                raise ValueError(f"Operador no válido: {op}")

            print(f"Resultado: {resultado}")
            return resultado

        except Exception as e:
            print(f"Error: {e}")