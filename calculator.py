# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

if __name__ == "__main__":
    print("Простой калькулятор на Python")
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")

    if op == '+':
        print("Результат:", add(x, y))
    elif op == '-':
        print("Результат:", subtract(x, y))
    elif op == '*':
        print("Результат:", multiply(x, y))
    elif op == '/':
        print("Результат:", divide(x, y))
    else:
        print("Неизвестная операция")
