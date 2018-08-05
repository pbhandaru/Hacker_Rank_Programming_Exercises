#!/usr/bin/python
import re
####
A = (5, 6, 7)
B = (3, 6, 10)
def solve(a, b):
    result = ''
    c = 0
    for i in range(len(a)):
	if a[i] > b[c] or a[i] < b[c]:
	    result += ' 1'
	elif a[i] == b[c]:
	    result += ' '
        c += 1
    return result

print solve(A, B)
