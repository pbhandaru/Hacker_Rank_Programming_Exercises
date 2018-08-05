#!/usr/bin/python
import sys
#>######
N = int(raw_input("Please enter an odd number: "))
M = 0
P='.|.'
i = 1
j = 0
if N % 2 != 0:
    if 5 < N < 101:
	M = N * 3
	if 15 < M < 303:
	    for x in range(1,N + 1):
	        if (N + 1) / 2 == x:
		    print '-' * int((M - 7)/2) + 'WELCOME' + '-' * int((M - 7)/2)
		elif x > (N + 1)/2:
		    i -= 2
		    while i >= 1:
			print '-' * (j/2) + P * i + '-' * (j/2)
			i -= 2
			j = M - len(P * i)
		    break
		else: 
		    j = M - len(P * i)
		    print '-' * (j/2) + P * i + '-' * (j/2)
		    i += 2
