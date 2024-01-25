##Arithmetic operators
x=5
y=5
print("Addition is:", x+y)
print("Substraction is:", x-y)
print("Multiplicatio is:", x*y)
print("Division is:", x/y)
print("Modulus is:", x%y)
print("Exponent is:", x**y)
print("Floor Division is:", x//y)

##Logical Operators
print(x==y and x>y)
print(x==y or x>y)
print(not(x==y and x>y))

##Solve Equation:(10*2+40/9-60+2)
print("(10*2+40/9-60+2) output of equation is:",10*2+40/9-60+2)

##Write a python program to accept value from user like name, salary then calculate the annual income of the employee.
name = input("Enter the employee's name: ") # Get the name and monthly salary from the user
monthly_salary = float(input("Enter the employee's monthly salary: "))
print("Name of the Employe is:",name)
print("Salary of the Employee is :",monthly_salary)
print("Annual Income of the Employee is: ",monthly_salary*12)
annual_income = monthly_salary * 12 # Calculate the annual income
print(f"The annual income of {name} is {annual_income}") # Print the result


##Write a python program to accept values from user like amount, time period and rate if interest and then calculate the simple interest.
A=int (input ("Enter the amount: "))
T=int (input ("Enter the Time period: "))
I=int (input ("Enter the rate of ineterest: "))
print ("Principal Amount is: ",A)
print ("Time Perios is: ", T,"yrs")
print ("Rate of Interest is: ", I)
print ("Simple Interest= ", A*T*I/100)

##Practical on control and for loop statements  
#❖ Find the final ticket price with the following conditions:  
#a) If men and senior citizen, 70% of fare is applicable  
#b) If female and senior citizen, 80% of fare is applicable  
#a) If female and normal citizen, 70% of fare is applicable  
#a) If men and normal citizen, 100% of fare is applicable Code
gender = input("Enter Gender (M/F) :")
senior_citizen = input("Are you a senior citizen? (Y/N) :")
fare = float(input("Enter the fare: "))
if gender == "M" and senior_citizen == "Y":
    price = 0.7 * fare
elif gender == "F" and senior_citizen == "Y":
    price = 0.8 * fare
elif gender == "F" and senior_citizen == "N":
    price = 0.7 * fare
elif gender == "M" and senior_citizen == "N":
    price = fare
else:
    print("Invalid input. Please enter the valid input")
print(f"Final ticket price: ${price:.2f}")


##Take a dataset for diabetes, Enter the 50 patient data and use for, if else statement.
dataset = [113,145,155,162,140,141,123,156,126,147,158,169,165,154,198,187,100,195,186,189,200,174,185,196,163,152,149,124,134,158,175,167,120,119,118,155,188,199,177]
for i in dataset:
    if i > 120:
        print("Blood sugar is High")
    elif i >= 100 and i <= 120:
        print("Blood sugar is Normal")
    else:
        print("Blood sugar is Low")


##Aim: ractical on while loop and break statements, Write a python program to find number series by adding +5. 
n = 0
number = int(input("Enter the Number: "))
while n <= number:
    print(n+5)
    n+=5
    print()

##Print a string “Hello world” except o using python while loop
text = "HELLO WORLD!"
length = len(text)
i = 0
while i < length:
    if text[i] != 'O':
        print(text[i], end="")
    i += 1


##Convert a number :a) decimal to binary  b) decimal to hexadecimal

#a) Decimal to Binary conversion
def decimal_to_binary (decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str (remainder) + binary
        decimal //= 2
    return binary
#b) Decimal to Hexadecimal conversion
def decimal_to_hexadecimal (decimal):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits [remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

choice=input ("Enter 'a' to convert to binary or 'b' to convert to hexadecimal: ")

if choice == 'a':
    decimal = int (input ("Enter a decimal number: "))
    binary = decimal_to_binary (decimal)
    print ("Binary representation: ", binary)
elif choice == 'b':
    decimal = int (input ("Enter a decimal number: "))
    hexadecimal = decimal_to_hexadecimal (decimal)
    print ("Hexadecimal representation: ",hexadecimal)
else:
    print("Invalid choice. Please enter 'a' or 'b.")
    

##Find the average of given number from user after finding average reverse the number.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
numbers = []
n = int(input("Enter the number of values: "))
for i in range(n):
    num = float(input(f"Enter value {i + 1}: "))
    numbers.append(num)
average = sum(numbers) / n
print("The average of the", n, "numbers is:", average)
reversed_average = reverse_number(int(average))
print(f"Reversed average: {reversed_average}")

##ractical on list, tuples, dictionary and functions  #Function in Python:
#Write a program to calculate the addition of two numbers.
def addition(a,b):
    c=a+b
    return  c
print("Addition = ",addition(30,40))

#Write a program to find the annual salary of an employee.
def annual_salary(salary):
    annual_sal=salary*12
    return  annual_sal
print("Annual Salary =", annual_salary(57000))

#Write a program to find the rate of interest for car loan, home loan and education.
def loan(total_interest, principal, yrs):
    rate = total_interest * 100 / principal * yrs
    return rate
print("1. Car Loan \n2. Home Loan \n3. Education Loan")
choice = int(input("Enter your choice: "))
if choice == 1:
    total_interest = float(input("Enter the total interest paid: "))
    principal = float(input("Enter the principal amount: "))
    yrs = int(input("Enter the number of years: "))
    print("Rate of interest of your car loan is: ", loan(total_interest, principal, yrs),"%")
elif choice == 2:
    total_interest = float(input("Enter the total interest paid: "))
    principal = float(input("Enter the principal amount: "))
    yrs = int(input("Enter the number of years: "))
    print("Rate of interest of your home loan is:", loan(total_interest, principal, yrs),"%")
elif choice == 3:
    total_interest = float(input("Enter the total interest paid: "))
    principal = float(input("Enter the principal amount: "))
    yrs = int(input("Enter the number of years: "))
    print("Rate of interest of your education loan is: ", loan(total_interest, principal, yrs),"%")
else:
    print("You have made a wrong choice.")







