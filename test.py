# name=input("Enter your name: ")
# print("Hello, " + name + "! Welcome to Python programming.")




input1 = input("Enter the first number  : ")
input2 = input("Enter the second number : ")

sum = int(input1) + int(input2)  # Convert the inputs to integers and calculate the sum

print("The sum of", input1, "and", input2, "is:", sum)





principal =input("Enter the principal amount: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time in years: ")

simple_interest = (float(principal) * float(rate) * float(time)) / 100  # Calculate simple interest
print("The simple interest is:", simple_interest)