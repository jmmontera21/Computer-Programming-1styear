print("\t\t Odd or Even")
print("\n")
first_number= int(input("Please enter the first number:"))
sec_number= int(input("Please enter the second number:"))
third_number= int(input("Please enter the third number:"))
print("\n")

odd_ = 0
even_ = 0
if (first_number % 2) == 0 :
	   print(f"The first number which is {first_number} is an even number")
    even_ += 1
if (first_number % 2) != 0 :
	   print(f"The first number which is {first_number} is an odd number")
    odd_ += 1

if (sec_number % 2) == 0 :
	   print(f"The second number which is {sec_number} is an even number")
    even_ += 1
if (sec_number % 2) != 0 :
	   print(f"The second number which is {sec_number} is an odd number")
	odd_ += 1

if (third_number % 2) == 0 :
	   print(f"The third number which is {third_number} is an even number")
    even_ +=1
if (third_number % 2) != 0 :
	   print(f"The third number which is {third_number} is an odd number")
    odd_ +=1
print("\t")
print(f"There are {even_} even number/s and {odd_} odd number/s")