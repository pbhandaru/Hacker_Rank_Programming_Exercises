#!/usr/bin/python
############

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
	line = raw_input().split()
	name, scores = line[0], line[1:]
	scores = map(float, scores)
	student_marks[name] = scores
    query_name = raw_input()
    if query_name in student_marks:
	avg = sum(student_marks[query_name])/float(len(student_marks[query_name]))
        #print round(avg, 2)
	print '%.2f' %(avg)
