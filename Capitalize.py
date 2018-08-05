#!/usr/bin/python
#############
s = 'alison heck'
res=s[0].upper()
count = 0
flag =1
for i in s[1:]:
    if i == ' ':
	res += i
        flag = 1
	continue
    elif flag:
	res += i.upper()
	flag = 0
    else:
	res += i
print res
	

