# Function-based Operations

def create_add_function(a, b):
    return a + b

def create_subtract_function(a, b):
    return a - b

def create_multiply_function(a, b):
    return a * b

def create_divide_function(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

# Main Program Flow

def calculator():
    print("Welcome to Simple Calculator")

    while True:
        print("\nChoose Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice.")
            continue

        # Get user numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Call the appropriate function
        if choice == '1':
            result = create_add_function(num1, num2)
        elif choice == '2':
            result = create_subtract_function(num1, num2)
        elif choice == '3':
            result = create_multiply_function(num1, num2)
        elif choice == '4':
            result = create_divide_function(num1, num2)

        print(f"Result: {result}")

# Run the calculator
calculator()
