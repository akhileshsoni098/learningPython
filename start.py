# Arithmetic and basic output
result = (2 + 5) * 3  # Calculate the result of (2+5)*3
print(result)  # Print the result
print(not 2 > 1)  # Print the negation of the comparison 2>1

# if-else statements
age = 3
if age >= 18:
    print("You are an adult")  # Print a message if age is greater than or equal to 18
    print("You can vote now")
elif 3 < age < 18:
    print("You are in school")  # Print a message if age is between 3 and 18 (exclusive)
else:
    print("You are a child")  # Print a message for any other age

print("Thank you")  # Print a final message

# Build a calculator
first = input("Enter your first digit: ")  # Take input for the first number
operator = input("Enter your operator (+, -, /, %): ")  # Take input for the operator
second = input("Enter your second digit: ")  # Take input for the second number

# Perform the calculation based on the operator
if operator == "+":
    print(float(first) + float(second))
elif operator == "-":
    print(float(first) - float(second))
elif operator == "*":
    print(float(first) * float(second))
elif operator == "/":
    print(float(first) / float(second))
elif operator == "%":
    print(float(first) % float(second))
else:
    print("Invalid entry")  # Print an error message for an invalid operator

# Range
num = range(5)  # Create a range from 0 to 4
print(list(num))  # Convert the range to a list and print it

# While loop
i = 6
while i >= 0:
    print(i * "*")  # Print '*' multiplied by the current value of i
    i -= 1  # Decrement the value of i by 1 in each iteration

# For loop
for i in range(1, 11):  # Iterate over the numbers from 1 to 10
    print(i)  # Print the current number

# Lists
marks = [95, 98, 97]  # Create a list of marks
print(marks[-1])  # Print the last element of the list
print(marks[-2])  # Print the second last element of the list
print(marks[1:3])  # Print elements at index 1 and 2

# Print all the marks in the list
for mark in marks:
    print(mark)

marks.append(99)  # Add 99 to the end of the list
print(marks)

marks.insert(1, 99)  # Insert 99 at index 1
print(marks)

print(99 in marks)  # Check if 99 exists in the list

print(len(marks))  # Print the length of the list

marks.clear()  # Clear the list
print(marks)  # Print an empty list

# Break and continue statements
stu = ["Ram", "Shyam", "Kishan", "Radha", "Radhika", "Rohan"]
for name in stu:
    if name == "Radha":
        break  # Exit the loop if the name is "Radha"
    print(name)

for name in stu:
    if name == "Radha":
        continue  # Skip the current iteration if the name is "Radha"
    print(name)

# Tuples
marks = (95, 98, 97, 97, 97, 99)  # Create a tuple of marks
print(marks.count(97))  # Count the number of occurrences of 97
print(marks.index(97))  # Find the index of the first occurrence of 97

# Sets
marks = {95, 98, 97, 97, 97, 99}  # Create a set of marks (unique values)
for mark in marks:
    print(mark)  # Print each mark in the set

# Dictionaries
marks = {
    "english": 95,
    "chemistry": 87,
    "physics": 88
}  # Create a dictionary of marks
print(marks["chemistry"])  # Print the value for the key "chemistry"
marks["math"] = 99  # Add a new key-value pair
print(marks)

# Functions
import math
print(dir(math))  # Print all the available functions in the math module

from math import sqrt
print(sqrt(9))  # Calculate the square root of 9

from math import *
print(sqrt(16))  # Calculate the square root of 16

# User-defined function
def multiply_by_five(x):  # Define a function that multiplies the input by 5
    print(x * 5)

multiply_by_five(6)  # Call the function with the argument 6

def print_sum(first, second):  # Define a function that prints the sum of two numbers
    print(first + second)

print_sum(4, 5)  # Call the function with arguments 4 and 5

def print_sum(first, second=7):  # Define a function with a default value for the second parameter
    print(first + second)

print_sum(4)  # Call the function with only the first argument
