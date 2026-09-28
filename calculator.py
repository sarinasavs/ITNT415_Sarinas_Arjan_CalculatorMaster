def get_number(prompt):
    """Prompt for a number, re-asking until valid."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 4 or 3.5).")

def print_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==============================")

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "5":
            print("Exiting Calculator Master. Goodbye!")
            break
        elif choice == "1":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            try:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()