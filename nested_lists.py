#!/usr/bin/python
#######
n = int(raw_input('Please enter the number of students'))
students = []
for i in range(n):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score]) 

print students
scores = []
for i in students:
    scores.append(i[1])

scores.sort()
print scores
second_lowest = 0
first_lowest = scores[0]
for i in scores:
    if i == first_lowest:
	continue
    elif i != first_lowest:
	second_lowest = i
	break

print second_lowest
    
result = []
for idx, val in enumerate(students):
    if val[1] == second_lowest:
	result.append(val[0])

if len(result) == 0:
    result.append(second_lowest)

for i in sorted(result):
    print i
