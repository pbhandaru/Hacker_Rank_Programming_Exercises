#!/usr/bin/python
########

num = raw_input('Please enter an 6 digit integer: ')
def validate_postal_codes(num):
    flag = 1 
    if len(str(num)) == 6: 
        for i in range(0,len(str(num))):
	    if str(num[i]) == str(num[i + 2]):
		flag = 0
		break
	    if i + 2 == len(str(num)) - 1:
	        break
    if flag:
	return True
    else:
	return False

#print validate_postal_codes('110000')
#print validate_postal_codes('121426')
#print validate_postal_codes('523563')
#print validate_postal_codes('552523')
print validate_postal_codes(num)
