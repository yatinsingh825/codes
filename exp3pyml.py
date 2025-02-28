print("Dipnshu 23BAI70028\n")

name = str(input("Enter the name: "))
roll_number = int(input("Enter the roll no.: "))


while True:
    maths = int(input("Enter maths marks: "))
    if maths>100 or maths<0:
        print("invalid choice")
    else:
        break
while True:
    science = int(input("Enter science marks: "))
    if science>100 or science<0:
        print("invalid choice")
    else:
        break
while True:
    english = int(input("Enter english marks: "))
    if english>100 or english<0:
        print("invalid choice")
    else:
        break


print("\nCALCULATING RESULTS...")
print("\nStudent Name: ",name)
print("Roll number: ",roll_number)
print("Marks: ",maths,science,english)

total = maths + science + english
print("Total marks = ",total)

avg = (maths + science + english)/3
print("Average Marks = ",avg)

percentage = ((total//300)*100)
print("Percentage = ",percentage,"%")


def pass_sub():
    if maths<40:
        print("student failed in maths")
    else:
        print("student passed in maths")

    if science<40:
        print("student failed in science")
    else:
        print("student passed in science")

    if english<40:
        print("student failed in english")
    else:
        print("student passed in english")
pass_sub()


if percentage>=75:
    print("Student qualifies for distinction")
else:
    print("Student didn't qualify for distinction")

def grade():
    if percentage>=85:
        print("Grade: A")
    elif percentage>=70 and percentage<=84:
        print("Grade: B")
    elif percentage>=50 and percentage<=69:
        print("Grade: C")
    elif percentage>=40 and percentage<=49:
        print("Grade: D")
    elif percentage<40:
        print("Grade: F")
grade()

def passed():
    if maths>40 and science>40 and english>40:
        print("Pass status: Passed")
    else:
        print("Not Passed and needs re-evaluation in the following subjects:")
        if not maths>40:
            print("Maths")
        if not science>40:
            print("Science")
        if not english>40:
            print("English")
passed()

print("Student ID: ",roll_number<<2)

