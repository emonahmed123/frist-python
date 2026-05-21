# print("Hello, World!")
# print("Welcome to the world of programming!")


# print(44+10)


#  Python uses indentation to define blocks of code. Make sure to use consistent indentation (e.g., 4 spaces) for your code.


 
#  learn variables 

# A variable name must start with a letter or an underscore (_) and can be followed by letters, digits, or underscores. Variable names are case-sensitive.don't start with a number and don't use special characters except for underscores.

# age = 25
# print(age)
# name = "Alice"
# print(name)
# _score = 90
# print(_score)

# print(id(age))  # This will give you the memory address of the variable 'age'
 
# con =True

# if con:
#     print("Condition is True")

# else:
#     print("Condition is False")


"""
This  type  under Numeric data type
1. int (integer) - represents whole numbers without a decimal point. Example: 5, -3, 0
2. float (floating-point) - represents numbers with a decimal point. Example: 3.14, -0.5, 2.0
3. complex - represents complex numbers with a real and imaginary part. Example: 2 + 3j, -1 - 4j
"""
import numbers


age = 20  #initzer data type
float_num = 3.14 #float data type
complex_num = 2 + 3j #complex data type


name = "Alice"  #string data type



# Sequence data types
# 1. list - an ordered, mutable collection of items. Example: [1, 2, 3], ['a', 'b', 'c']

# city= ["New York", "Los Angeles", "Chicago"]  #list data type

# print(city[0])  # Accessing the first element of the list


# 2. tuple - an ordered, immutable collection of items. Example: (1, 2, 3), ('a', 'b', 'c')

# numbers = (1, 2, 3)  #tuple data type

"""
sd

"""

# 3. range - represents a sequence of numbers. Example: range(0, 10) represents numbers from 0 to 9

# numbers = range(0, 10, 3)  #range data type
# print(numbers)  # This will print the range object, not the actual numbers
# print()

# # To see the actual numbers, you can convert the range to a list
# print(*numbers)

 #  Map data type
# 1. dict (dictionary) - an unordered collection of key-value pairs. Example: {'name': 'Alice', 'age': 25}


# set data type
# 1. set - an unordered collection of unique items. Example: {1, 2, 3}, {'a', 'b', 'c'}

# unique_numbers = {1, 2, 3, 4, 5}  #set data type
# print(unique_numbers)

# unique_numbers={"apple", "banana", "orange", "apple"}  #set data type
# print(unique_numbers)  # This will print {'apple', 'banana', 'orange'} because sets do not allow duplicate values

# unique_number=frozenset([1, 2, 3, 4, 5])  #frozenset data type

try:
   name = "Alice"
   x=int(name)  # This will raise a ValueError because "Alice" cannot be converted to an integer
   print(x)
except Exception as e:
    print(f"An error occurred: {e}")