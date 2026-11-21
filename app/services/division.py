def divide_numbers(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ValueError("Cannot divide by zero")

    return num1 / num2