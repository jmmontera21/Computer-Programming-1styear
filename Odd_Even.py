print("\t\t\t ??????????????????")
print("\t\t\t Odd or Even Number")
print("\t\t\t !!!!!!!!!!!!!!!!!!")
print("\t")
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
third_number = int(input("Please enter the third number: "))
print("\t")

odd_ = 0
even_ = 0
if (first_number % 2) == 0 :
	print(f"The first number which is {first_number} is an even number")
	even_ += 1
if (first_number % 2) != 0 :
	print(f"The first number which is {first_number} is an odd number")
	odd_ += 1

if (second_number % 2) == 0:
	print(f"The second number which is {second_number} is an even number")
	even_ += 1
if (second_number % 2) != 0 :
	print(f"The second number which is {second_number} is an odd number")
	odd_ += 1

if (third_number % 2) == 0 :
	print (f"The third number which is {third_number} is an even number")
	even_ += 1
if (third_number % 2) != 0 :
	print(f"The third number which is {third_number} is an odd number")
	odd_ += 1
print("\t")
print("\t")
print(f"There are {even_} even number and {odd_} odd number")