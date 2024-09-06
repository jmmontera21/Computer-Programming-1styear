print("\t" "Grading System")

prelim = int(input("Please enter your Prelim Grade:"))
midterm = int(input("Please enter your Midterm Grade:"))
final = int(input("Please enter your Final Grade:"))

average = prelim + midterm + final
a_average = average / 3


if prelim <55:
    print(f"You're prelim Grade which is {prelim} is below 55 not valid")
elif prelim >95:
    print(f"You're prelim grade which is {prelim} is above 95 not valid")
if midterm <55:
    print(f"You're midterm grade which is {midterm} is below 55 not valid") 
elif midterm >95:
    print(f"You're midterm grade which is {midterm} is above 95 not valid")
if final <55:
    print(f"You're final grade which is {final} is below 55 not valid")
elif final >95:
    print(f"You're final grade which is {final} is above 95 not valid")

else:
    if a_average <75:
        print(f"Sorry you failed the course with a general averagr of {a_average}")
    elif a_average >=75:
        print(f"Congratulation you passed the course with a general average of {a_average}")