grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
grade1=list(grade_one.keys())
grade2=list(grade_two.keys())
grade3=list(grade_three.keys())
count1=len(grade1)
count2=len(grade2)
count3=len(grade3)
print("Choose one: students_names, students_score, students_count")
grade_name=input('Enter grade_name: ')
def students_names(grade_name):
    x= list(grade_name.keys())
    return x
if grade_name=="grade_one":
    print(grade1)
elif grade_name=="grade_two":
    print(grade2)
elif grade_name=="grade_three":
    print(grade3)

grade=input('Enter grade: ')
students_names=input('Enter students names: ')
a=grade_one.get('students_names')
def students_score (grade,students_names):
    if grade== grade_one:
        return grade1
    elif grade== grade_two:
        return grade2
    elif grade== grade_three:
        return grade3
    if grade=="grade_one":
        a=grade_one.get('students_names')
        score=a.sum()
    elif grade=="grade_two":
        a=grade_two.get('students_names')
        score=a.sum()
    elif grade=="grade_three":
        a=grade_three.get('students_names')
        score=a.sum()
    return score
print(students_score(grade,students_names))
print(score)

grade=input('Enter grade_name: ')
def students_count(grade_name):
    count=len(grade_name)
    if grade==grade_name:
        print(count1)
    elif grade==grade_two:
        print(count2)
    elif grade==grade_three:
        print(count3)
    return count

y="more"
i=input('enter next: ')
while i==y:
    print("Choose one: students_names, students_score, students_count")
    break
else:
    print("Done")
