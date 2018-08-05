#!/usr/bin/python
##########
def minion_game(string):
    vs=0
    cs=0
    V='AEIOU'
    for i in range(len(string)):
        if string[i] in V:
            vs += len(string[i:])
        else:
            cs += len(string[i:])
    if vs > cs:
        print 'Kevin', str(vs)
    elif vs < cs:
        print 'Stuart', str(cs)
    elif vs == cs:
        print 'Draw'

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
