# Here we use some operators

def add(x, y):
    return x + y

def subtract(x ,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x ,y):
    if y == 0 :
        return "Y cannot be divided by zero"
    return x / y



# Here we define function with while loop 
def calculator():
    while True:
        print("----- THIS IS THE CLI CALCULATOR WHERE U CAN PERFORM BASIC CALCULATIONS -----")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # This is user input
        user = int(input("Enter the number you want from choice from (1 - 5): "))

        # If 5 by user it will break program 
        if user == 5:
            print("Thanks for using calculator!!!")
            break

        # If 1,2,3,4,5 based on the user choice
        if user in (1, 2, 3, 4, 5):
            # It try the code execution 
            try:
                num1 = int(input("Enter the number 1: "))
                num2 = int(input("Enter the number 2: "))

            # It handles the error
            except ValueError:
                # print(v)
                print("You have written invalid input, Please enter the number only not letters !!!!")
                continue


            if (user == 1):
                operator = "+"
                Output = add(num1, num2)

            elif(user == 2):
                operator = "-"
                Output = subtract(num1, num2)

            elif(user == 3):
                operator = "*"
                Output = multiply(num1, num2)

            elif(user == 4):
                operator = "/"
                Output = divide(num1, num2)

            print(f"Output:{Output} \n")


            with open("history.txt",'a') as f:
                f.write(f"{num1} {operator} {num2} : {Output} \n")

        else:
            print("Invalid choice !!! please select from (1 - 5)")


# It runs the program 
if __name__ == "__main__":
    calculator()
