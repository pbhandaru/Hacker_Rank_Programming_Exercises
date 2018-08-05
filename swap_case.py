#!/usr/bin/python
#########

#def swap_case(s):

A='HackerRank.com presents "Pythonist 2".'
for i in A:
    if i.isspace() or i.isdigit():
	continue    
    if i.isupper():
	print i
	print i.lower()
    else:
	if i.islower():
	    print i
	    print i.upper()
