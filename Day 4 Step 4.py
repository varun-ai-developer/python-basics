def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid Operator"
    
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculator(x, y, op)
print("Result:", result)