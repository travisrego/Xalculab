print("Welcome to Xalculab - a Calculator made with Python")
print("Type quit anytime to quit the application")

def performArithmetic():
    while True:
        operation = input("Please type an operation: ")
        if (operation == "quit"):
            print("Thank you for using Xalculab.")
            exit()
        if operation == "+" or operation == "add":
            print(int(number1) + int(number2))
            break
        elif operation == "-" or operation == "subtract":
            print(int(number1) - int(number2))
            break
        elif operation == "*" or operation == "multiply":
            print(int(number1) * int(number2))
            break
        elif operation == "/" or operation == "divide":
            print(int(number1) / int(number2))
            break
        else:
            print("Invalid operation, Please type a valid operation")
            continue      

while True:
    while True:
        usrInput1 = input("Please type a number: ")  
        if (usrInput1 == "quit"):
            print("Thank you for using Xalculab.")
            exit()
        try:
            number1 = int(usrInput1)
            break
        except:
            print("Please type a numeric value")
    
    while True:
        usrInput2 = input("Please type another number: ")
        if (str(usrInput2) == "quit"):
            print("Thank you for using Xalculab.")
            exit()
        try:
            number2 = int(usrInput2)
            break
        except:
            print("Please type a numeric value")
            
    performArithmetic()





