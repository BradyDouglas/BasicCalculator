def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    return a / b

doSelect = True
hasRan = False
displayNumber = "Enter a number"
displayOperation = "Enter an operation"
result = 0

while doSelect:
    if hasRan == False:
        print (displayNumber)
        num1 = input()
    else:
        num1 = result

    print (displayOperation)
    op = input()

    print (displayNumber)
    num2 = input()

    if op == "+":
        result = Add(float (num1), float (num2))
    elif op == "-":
        result = Subtract(float (num1), float (num2))
    elif op == "*":
        result = Multiply(float (num1), float (num2))
    elif op == "/":
        result = Divide(float (num1), float (num2))
    
    print (result)

    print ("Would you like to continue? Y/N")
    
# can also do "cont = input().upper()"

    cont = input()
    cont = cont.upper()

    if cont == "Y" or cont == "y":
        doSelect = True
        hasRan = True
    elif cont == "N" or cont == "n":
        doSelect = False

print (f"Final result: {result}")