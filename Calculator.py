class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "Error! Division by zero."
        return self.num1 / self.num2

    def power(self):
        return self.num1 ** self.num2

    def exit(self):
        return "Exiting..."


if __name__ == '__main__':
    print("Hello From Our Calculator App")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    calculator = Calculator(num1, num2)


    def show_menu():
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Exit")


    while True:
        show_menu()
        choice = input("Enter operation: ")

        if choice == "1":
            print("Result:", calculator.addition())
        elif choice == "2":
            print("Result:", calculator.subtraction())
        elif choice == "3":
            print("Result:", calculator.multiplication())
        elif choice == "4":
            print("Result:", calculator.division())
        elif choice == "5":
            print("Result:", calculator.power())
        elif choice == "6":
            print(calculator.exit())
            break
        else:
            print("Invalid choice. Please try again.")
