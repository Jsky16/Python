#Program for minimum of 3 numbers using ternary operator
num_first=int(input("Enter first number here: "))
num_second=int(input("Enter second number here: "))
num_third=int(input("Enter third number here: "))
min_value=num_first if num_first < num_third and num_first < num_second else num_second if num_second < num_third else num_third
print("minimum among three given number is: ",min_value)