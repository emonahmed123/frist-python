# name=input("Enter your name: ")
# print("Hello, " + name + "! Welcome to Python programming.")




# input1 = input("Enter the first number  : ")
# input2 = input("Enter the second number : ")

# sum = int(input1) + int(input2)  # Convert the inputs to integers and calculate the sum

# print("The sum of", input1, "and", input2, "is:", sum)





# principal =input("Enter the principal amount: ")
# rate = input("Enter the rate of interest: ")
# time = input("Enter the time in years: ")

# simple_interest = (float(principal) * float(rate) * float(time)) / 100  # Calculate simple interest
# print("The simple interest is:", simple_interest)


# Strings in Python are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). You can use any of these to define a string, but they must be consistent. For example:
# string1 = 'Hello, World!'  # Using single quotes
# string2 = "Welcome to Python programming!"  # Using double quotes 
# string3 = '''This is a string with triple quotes.'''  # Using triple quotes

# text = "Hello, World!"
# print(text[:6])  # Output: Hello


# print(text[0::2])  # Output: Hlo ol!

# name = "Alice "

# repate = name * 3
# print(repate)  # Output: Alice Alice Alice 

# concationation = name + "Smith"
# print(concationation)  # Output: Alice Smith

# string1 = "Hello, "
# string2 = "World!"
# concatenated_string = string1 + string2
# print(concatenated_string)  # Output: Hello, World!

# combined_string = "".join([string1, string2])
# print(combined_string)  # Output: Hello, World!

# combine ="{} {}".format(string1, string2)
# print(combine)  # Output: Hello, World!




#Stirng methods
text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!
print(text.lower())  # Output: hello, world!
print(text.capitalize()) # Output: Hello, world!
print(text.title())  # Output: Hello, World!
print(text.strip())  # Output: Hello, World! (removes leading and trailing whitespace)
print(text.lstrip())  # Output: Hello, World! (removes leading whitespace)
print(text.rstrip())  # Output: Hello, World! (removes trailing whitespace)
print(text.replace("World", "Python"))  # Output: Hello, Python!
print(text.swapcase())  # Output: hELLO, wORLD!
print(text.split(", "))  # Output: ['Hello', 'World!'] (splitsvvb

# check if srting with a substring

print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))  # Output: True

text.find("World")  # Output: 7 (returns the index of the first occurrence of "World" )

text.count("o")  # Output: 2 (counts the number of occurrences of "o" in the string)

text.isalpha()  # Output: False (checks if all characters in the string are alphabetic)
text.isalnum()  # Output: False (checks if all characters in the string are alphanumeric)
text.isdigit()  # Output: False (checks if all characters in the string are digits)

text.isspace()  # Output: False (checks if all characters in the string are whitespace)
text.istitle()  # Output: True (checks if the string is in title case)  

sentence = " This is a sample sentence. "

sentence.title()  # Output: This Is A Sample Sentence. (converts the string to title case)
sentence.strip().title()  # Output: This Is A Sample Sentence. (removes leading and trailing whitespace)


a=10
b=20
print(a+b)  # Output: 30 (performs addition)
print(a-b)  # Output: -10 (performs subtraction)  
print(a*b)  # Output: 200 (performs multiplication)
print(a/b)  # Output: 0.5 (performs division)
print(a//b)  # Output: 0 (performs floor division)
print(a%b)  # Output: 10 (performs modulus)
print(a**b)  # Output: 100000000000000000000 (performs exponentiation)

#Type Conversion:

num_str = "123"
num_int = int(num_str)  # Convert string to integer