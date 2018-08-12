#!/usr/bin/python
#######
def text_wrap(s, width):
    res = ''
    i = 0
    if len(s) <= width:
	return s
    elif len(s) > width:
	while i < len(s):
	    res += s[i:i + width] + '\n'
	    i += width 
    res = res.rstrip('\n')
	    
    if i > len(s):
	res += s[i:]
    return res

# Sampple Inputs
print text_wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
print text_wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 5)
print text_wrap('ABCDE', 5)
print text_wrap('ABCDE', 4)
#####


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
