print("\t\t\t Grading System")

grades = int (input("Please enter your final grade: "))

#passing grade 80

if grades >= 80:
	print("Congratulation you pass")
	ad_python = int (input("Please enter your grades in advanced python: "))
	if ad_python >= 75:
		print("You are a certified pythonista")
	elif ad_python < 75:
		print("Retake advanced python")

elif grades < 80:
	print("Sorry, you failed")
	print("You are not qualified to take advanced python")