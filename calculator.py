# simple daily use calculator
def operands():
    while True:
        num1 = (input("Enter the number: "))
        try:
            return float(num1)
            break
        except:
            print("Invalid number,try again")


is_valid = True
output = 0
while is_valid:
    operand1 = operands()
    sign = input("Enter the operation to be done(+,-,/,*): ")
    operand2 = operands()
    
    if sign == "+":
        output = operand1 + operand2
        break
    elif sign == "-":
        output = operand1 - operand2
        break
    elif sign == "*":
        output = operand1 * operand2
        break
    elif sign == "/":
        if operand2 == 0:
            print("Division by zero")
        else:
            output =  operand1 / operand2
        break
    else:
        print("Invalid sign")
        
print(f"{operand1}| {sign} |{operand2} ")
print(f"The result is {output}")