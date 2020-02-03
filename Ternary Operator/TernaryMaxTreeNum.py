#Program for maximum of 3 numbers using ternary operator
num_first=int(input("Enter first number here: "))
num_second=int(input("Enter second number here: "))
num_third=int(input("Enter third number here: "))
max_value=num_first if num_first>num_second and num_first>num_third else num_second if num_second > num_third else num_third
print("maximum among three given number is: ",max_value)