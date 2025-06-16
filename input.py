def get_integer_list():
    while True:
        user_input = input("Enter at least 2 integers separated by spaces (last number should not be 0): ")
        try:
            # Convert input to list of integers
            int_list = [int(x) for x in user_input.strip().split()]
            
            # Check conditions
            if len(int_list) < 2:
                print("Please enter at least 2 integers.\n")
            elif int_list[-1] == 0:
                print("The last number must not be 0. Try again.\n")
            else:
                return int_list
        except ValueError:
            print("Invalid input. Please enter only integers.\n")

# Example usage
numbers = get_integer_list()
print("You entered:", numbers)
