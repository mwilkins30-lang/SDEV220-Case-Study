quit = "ZZZ"
deans_list = {}
honor_roll = {}
rest_of_best = []
student_last_name = ""
while student_last_name != quit:
    student_last_name = input("Enter student last name (or ZZZ to quit): ")
    if student_last_name == quit:
        break
    student_first_name = input("Enter student first name: ")
    student_GPA = float(input("Enter student GPA: "))
    if student_GPA >= 3.5:
        deans_list[student_last_name] = student_first_name
    elif student_GPA >= 3.25 and student_GPA < 3.5:
        honor_roll[student_last_name] = student_first_name
    else:
        rest_of_best.append((student_last_name, student_first_name, student_GPA))

else:
    print("Please enter a valid last name or type ZZZ to quit." )

for last_name, first_name in deans_list.items():
    print(f"{first_name} {last_name} is on the Dean's List.")
for last_name, first_name in honor_roll.items():
    print(f"{first_name} {last_name} is on the Honor Roll.")
for last_name, first_name, GPA in rest_of_best:
    print(f"{first_name} {last_name} has a GPA of {GPA}.")

