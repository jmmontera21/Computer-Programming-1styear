print("\t\t Odd and Even")

number = int(input("Please enter your number: "))

ans = int(number % 2)

if ans == 0:
	print("It is an even number".format(number))
elif ans > 0:
	print("It is an odd number".format(number))