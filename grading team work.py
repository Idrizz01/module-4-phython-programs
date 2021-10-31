# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #int was missing

exam_three = int(input("Input exam grade three: ")) #the three was in numbers instead of letters, instead of str we changed it to int

grades = [exam_one, exam_two, exam_three] #commas were missing after exam_one and exam_two
sum = 0
for grade in grades:   #an s was missing after grade
  sum = sum + grade

avg = sum / len(grades)  #grades was spelt wrong

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added a semicolon at the end of 90
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"    #the right quotation was missing after the letter C
'''
Logic error: Use a proper range for the average.

If the average is in the range  of 60 <= avg < 70, letter_grade is "D."
If the average is in the range of 0<= avg < 60, letter_grade is "F."

elif avg >= 60 and avg < 70:
     letter_grade = "D"
elif avg >= 0 and avg < 60:
     letter_grade = "F"
     
'''
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif avg <= 65 and avg >= 0: #removed the semicolon in fornt of the elif and added an expression instead 
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
    
'''
Print the average and letter grade out of the for loop.
Syntax error: No indentation for print statements

print("Average: " + str(avg))
print("Grade: " + str(letter_grade))
'''
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":   #changed - to _
    print ("Student is failing.")  #both parenthesis were missing
else:
    print ("Student is passing.")   #both parenthesis also missing 
