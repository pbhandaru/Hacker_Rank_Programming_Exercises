#!/usr/bin/python
###########
n = 18
w = len("{0:b}".format(n))
for i in range(1,18):
    print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w)
