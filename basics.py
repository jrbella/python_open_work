import datetime
print("The date and time is:", datetime.datetime.now())


#average score
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

#Find the mean
student_aggregate = sum(student_grades.values())
length = len(student_grades)
mean = student_aggregate / length
print("The average grade is %s" % (mean))