grade = int(input("Enter the grade level number:"))
grade_level = None

if 18 >= grade >= 1:
    if 1 <= grade <= 5:
        grade_level = "Elementary school"
    elif 6 <= grade <= 8:
        grade_level = "Middle school"
    elif 9 <= grade <= 12:
        grade_level = "High school"
    elif 13 <= grade <= 16:
        grade_level = "College"
    else:
        grade_level = "Grad school"
else:
    grade_level = "Invalid grade level"

print(grade_level)