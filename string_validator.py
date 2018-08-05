#!/usr/bin/python
##########
def str_validate(s):
#    a = 0
#    d = 0
#    u = 0
#    l = 0
#    x = 0
    a, d, u, l, x = 0, 0, 0, 0, 0 
    if s.isalnum():
	print 'True'
    else:
	print 'False'

    for i in s:
	if i.isalpha():
	    a = 1 
	if i.isdigit():
	    d = 1
	if i.isupper():
	    u = 1
	if i.islower():
	    l = 1
        x += a + d + u + l
	if x == 4:
	    break 

    if a:
	print 'True'
    else:
	print 'False'
    if d:
	print 'True'
    else:
	print 'False'
    if l:
	print 'True'
    else:
	print 'False'
    if u:
	print 'True'
    else:
	print 'False'

str_validate('qA2')

print '-------\n'
