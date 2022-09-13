
#todo:  Approach 1 (Naive)
def grading_students(grades):
    result = []
    for grade in grades:
        compied_grade = grade
        while grade %5 != 0 and grade >37:
            grade += 1
        difference = grade - compied_grade
        if difference < 3:
            result.append(grade)
        else:
            result.append(compied_grade)
    return result


grades = [73,67,38,33]
print("Approach 1: ",grading_students(grades))
#! Expected result:  75 67 40 33

#todo: Approach 2 (Much better in time complexity)
def grading_students2(grades):
    result = []
    for grade in grades:        
        if  grade > 37 and grade %5 >= 3:
            grade = grade + (5 - grade %5  )
            result.append(grade)
        else:
            result.append(grade)
    return result
print("Approach 2: ",grading_students(grades))



