#Read two numbers from the keyboard and print minimum value using ternary operator
num_first=int(input("Enter the first number: "))
num_second=int(input("Enter the second number: "))
minm=num_first if num_first<num_second else num_second
print("minimum value from the given input is: ",minm)
