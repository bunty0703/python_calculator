import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Trigonometric Functions (sin, cos, tan)")
    print("8. Logarithm")
    print("9. Quit")

    while True:
        choice = input("Enter operation number (1-9): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 + num2)
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 - num2)
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 * num2)
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", num1 / num2)
        elif choice == '5':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", base ** exponent)
        elif choice == '6':
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))
        elif choice == '7':
            function = input("Enter function (sin/cos/tan): ")
            angle = float(input("Enter angle in degrees: "))
            if function == 'sin':
                print("Result:", math.sin(math.radians(angle)))
            elif function == 'cos':
                print("Result:", math.cos(math.radians(angle)))
            elif function == 'tan':
                print("Result:", math.tan(math.radians(angle)))
            else:
                print("Invalid function!")
        elif choice == '8':
            num = float(input("Enter number: "))
            print("Result:", math.log(num))
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    scientific_calculator()
