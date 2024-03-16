from art import logo

def Addition(num1, num2):
    return num1+num2

def Multiplication(num1, num2):
    return num1*num2

def Subtraction(num1, num2):
    return num1-num2

def Division(num1, num2):
    return num1/num2

operation = {
    "+":Addition,
    "-":Subtraction,
    "*":Multiplication,
    "/":Division
}
def calculator():
    print(logo)
    should_continue = True
    num1  = int(input("What's the first Number?: "))
    
    for symbol in operation:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an Operation : ")  
        num2  = int(input("What's the Next Number?: "))
        calculation_function = operation[operation_symbol]
        result=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"type 'Y' to continue calculatin with the {result}, or type 'N' to start a new calculation: ") == 'Y':
            num1 = result
        else:
            should_continue = False
            calculator()        
    

calculator()



