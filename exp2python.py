def classify_input(number):
    if number < 13:
        return "Age category is Child."
    elif 13 <= number <= 19:
        return "Age category is Teenager."
    elif 20 <= number <= 59:
        return "Age category is Adult."
    else:
        return "Age category is Senior."

def display_even_odd_numbers(value):
    if(value%2==0):
        print(f"{value} is even")
    else:
        print(f"{value} is odd")
    
    

def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def main():
    print("Dipanshu 23BAI70028")
    while True:
        print("\nMenu:")
        print("1. Classify Input")
        print("2. Display Even/Odd Numbers")
        print("3. Calculate Factorial")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            number = int(input("Enter an integer: "))
            print("Output:", classify_input(number))
        elif choice == 2:
            value = int(input("enter the nuumber"))
            display_even_odd_numbers(value)
            
        elif choice == 3:
            number = int(input("Enter a number: "))
            print(f"Output: The factorial of {number} is {calculate_factorial(number)}.")
        elif choice == 4:
            print("Output: Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
