#!/usr/bin/python
################
N = int(raw_input())
i = 0
L = []
while i <= N:
    F=raw_input().split()
    i += 1
    if F[0] == 'insert':
	L.insert(int(F[1]), int(F[2]))
    elif F[0] == 'append':
	L.append(int(F[1]))
    elif F[0] == 'print':
	print L
    elif F[0] == 'remove':
	L.remove(int(F[1]))
    elif F[0] == 'sort':
	L.sort()
    elif F[0] == 'pop':
	L.pop()
    elif F[0] == 'reverse':
	L.reverse()
    if str(i) == str(N):
	break
