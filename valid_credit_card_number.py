#!/usr/bin/python
import re
####################

def check_if_credit_card_number_is_valid_or_not(num):
    if ' ' in num:
	return 'InValid'
    flag = 0
    if len(num) == 16 or len(num) == 19:
	i = 0
	if re.search('^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', num):
	    if len(num) == 19:
		num = ''.join(re.split('-', num))
	    for e in range(len(num)):
		if num[i] * 4 == num[i:i+4]:
		    flag = 1
		    break
	        i += 1
	    if flag:
	        return 'Invalid'
	    else:
		return 'Valid'
	else:
	    return 'Invalid'
    elif re.search('^[0-9A-Za-z]{17,}', num):
	return 'Invalid'
    elif not re.search('^[4-6]', num):
	return 'Invalid'
    elif len(num) < 16 or len(num) > 19:
	return 'Invalid'

#for i in ['4253625879615786', '4424424424442444', '5122-2368-7954-3214', '42536258796157867', '4424444424442444', '5122-2368-7954 - 3214', '44244x4424442444', '0525362587961578']: 
#    print check_if_credit_card_number_is_valid_or_not(i)

#print '-----------\n---------\n'
#for i in ['4123456789123456', '5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456', '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456']:
#    print check_if_credit_card_number_is_valid_or_not(i)

inputs=[]
n = int(raw_input())
for i in range(n):
    s=str(raw_input())
    inputs.append(s)

for i in inputs:
    print check_if_credit_card_number_is_valid_or_not(i)
