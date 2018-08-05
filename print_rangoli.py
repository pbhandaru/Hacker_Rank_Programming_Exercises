#!/usr/bin/python
import string
##########
N=int(raw_input())
mid = N - 1
for i in range(N-1, 0, -1):
    row = ['-'] * (2 * N - 1)
    for j in range(N-i):
	row[mid-j] = row[mid+j] = string.ascii_lowercase[j+i]
    print '-'.join(row)

for i in range(N):
    row = ['-'] * (2 * N - 1)
    for j in range(N-i):
	row[mid-j] = row[mid+j] = string.ascii_lowercase[j+i]
    print '-'.join(row)
