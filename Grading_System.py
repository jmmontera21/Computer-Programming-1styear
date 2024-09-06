print("\t\t\t %%%%%%%%%%%%%%")
print("\t\t\t Grading System")
print("\t\t\t %%%%%%%%%%%%%%")
print("\t")
a_grades = int (input("Please enter your Prelim grades: "))
b_grades = int (input("Please enter your Midtem grades: "))
c_grades = int (input("Please enter your Finals grades: "))


if a_grades < 55:
	print(f" Your Prelim grade which is {a_grades} is below 55 not valid ")
if a_grades > 95:
	print(f" Your Prelim grade which is {a_grades} is above 95 not valid ")
if b_grades < 55:
	print(f" Your Midterm grade which is {b_grades} is below 55 not valid ")
if b_grades > 95:
	print(f" Your Midterm grade which is {b_grades} is above 95 not valid ")
if c_grades < 55:
	print(f" Your Finals grade which is {c_grades} is below 55 not valid ")
if c_grades > 95:
	print(f" Your Finals grade which is {c_grades} is above 95 not valid ")

else: 
	if (a_grades + b_grades + c_grades) / 3 > 75:
		print(f"Congratulations you passed the course with a general average of {(a_grades + b_grades + c_grades) / 3}")
	else:
		print(f"Sorry you failed the course with a general average of {(a_grades + b_grades + c_grades) / 3}")
	

