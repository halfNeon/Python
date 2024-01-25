##Practical on exception handling and file handling: #File Handling Operation in Python:  
#1)Open file:# Open file
f = open("my_file.txt")
print(f.closed)

#2)Read:# Read file
file1 = open("example.txt", "r")
read_content = file1.read()
print(read_content)
file1.close()

#3)Write:# Write to file
file1 = open("example.txt", "w")
file1.write("Hello!....")
file1.close()
file1 = open("example.txt", "r")
print(file1.read())

#4)Append:# Append to file
file1 = open("example.txt", "a")
file1.write("Now the file has more content!")
file1.close()
file1 = open("example.txt", "r")
print(file1.read())

#5)Exclusive creation:# Exclusive creation (creates a new file only if it doesn't exist)
f = open("my_file.txt", "x")

#6)close file:# Close file
f = open("my_file.txt")
# Operations on the file...
f.close()

#Note: It's a good practice to use the with statement when working with files, as it automatically closes the file when the block is exited, even if an exception occurs. Example:
with open("my_file.txt", "r") as f:
    # Operations on the file...
# File is automatically closed outside the 'with' block.

    

## Exception Handling in Python

# Q.1. Accept the value from the user's age to check if it is valid for voting or not.
try:
    # Accepting user input for age
    age = int(input("Enter your age: "))

    # Checking if the age is valid for voting
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

except Exception as e:
    print("An error occurred:", e)

    

# Q.2. Accept the value from the user's age to check if it is a senior citizen or not.
try:
    # Accept the age from the user
    age = int(input("Enter your age: "))

    # Check if the age is within a valid range
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")

except ValueError:
    print("Invalid input. Please enter a valid age as a number.")

except Exception as e:
    print("An error occurred:", e)
    
#Q.3. Accept experience and salary from employee if experience is 5+ then 15% increment in salary.
    class InvalidInputError(Exception):
    pass

def calculate_salary_increment(experience, current_salary):
    try:
        # Validate input for experience
        if not isinstance(experience, int) or experience < 0:
            raise InvalidInputError("Experience should be a non-negative integer.")

        # Validate input for current salary
        if not isinstance(current_salary, (int, float)) or current_salary < 0:
            raise InvalidInputError("Current salary should be a non-negative number.")

        # Check if the employee has 5 or more years of experience
        if experience >= 5:
            # Apply a 15% increment in salary
            new_salary = current_salary * 1.15
            return new_salary
        else:
            return current_salary

    except InvalidInputError as e:
        print(f"Invalid input: {e}")
        return None

try:
    experience_input = int(input("Enter years of experience: "))
    salary_input = float(input("Enter current salary: "))
    
    incremented_salary = calculate_salary_increment(experience_input, salary_input)
    
    if incremented_salary is not None:
        print(f"New salary: ${incremented_salary:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")

