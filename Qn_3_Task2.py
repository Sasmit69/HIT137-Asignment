# Define a global variable
global_variable = 100

# Initialize a dictionary with some key-value pairs
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    # Indicate that we will use the global variable
    global global_variable
    
    # Set a local variable
    local_variable = 5
    
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # Update the list based on the local variable
    while local_variable > 0:
        if local_variable % 2 == 0:
            # Remove the even number from the list if it's present
            if local_variable in numbers:
                numbers.remove(local_variable)
        local_variable -= 1
    
    # Print the updated list
    print(numbers)

def modify_dict():
    # Define a local variable within this function
    local_variable = 10
    
    # Add a new entry to the global dictionary
    my_dict['ke14'] = local_variable

def update_global():
    # Change the global variable
    global global_variable
    global_variable += 10

# Call the functions
process_numbers()
modify_dict()
update_global()

# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Check conditions and print messages accordingly
if my_dict.get('ke14') == 10:  # Access the dictionary safely
    print("Condition met!")

if 5 not in my_dict:
    print("5 is not found in the dictionary!")

# Output the final values of the variables
print(global_variable)
print(my_dict)
print({1, 2, 3, 4, 5})
