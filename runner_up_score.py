#!/usr/bin/python
########
n = int(raw_input())
arr = map(int, raw_input().split())
mx = 0
d = {}
unq = []
if len(arr) == n:
    for i in arr:
	if not i in d:
	    d[i] = 1
	    unq.append(i)
	else:
	    d[i] += 1

print sorted(unq)[-2] 
## Using List Comp

uniq = [x for x in arr if arr.count(x) == 1] 
print uniq
