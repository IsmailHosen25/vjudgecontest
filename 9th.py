def gradingStudents(grades):
    for i in range(0,len(grades)):
        
        if grades[i] < 38:
            continue
        else:
            temp = grades[i]
            te = temp % 5
            if te == 3:
                temp = temp + 2
                grades[i] = temp
            elif te == 4:
                temp = temp + 1
                grades[i] = temp
            else:
                continue
    return grades

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

result = gradingStudents(grades)
for i in result:
     print(i)