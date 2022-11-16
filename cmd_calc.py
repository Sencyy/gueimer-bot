# cmd_calc.py

def calc(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        result = "pqp man sabe nem o sinal de mais"

    return(result)
    
