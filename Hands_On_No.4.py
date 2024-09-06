print("\t")
print("\t\t\t======================")
print("\t\t\t| Money Denomination |")
print("\t\t\t======================")
print("\t")

print("This program will display all the denomination for your money")
print("\t")
nominals = (1000, 500, 200, 100, 50, 10, 1)
amount = int(input('Please enter the amount of money you have : '))
print("\t")
output = {}
for n in nominals:
	output[n] = amount // n
	amount %= n
for k, v in output.items():
	print(k, v, sep=' peso bill: ')