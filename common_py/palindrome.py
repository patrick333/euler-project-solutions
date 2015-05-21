#!/usr/bin/python
from math import ceil

def isPalin(str):
	l=len(str)
	for i in range(0,l/2):
		# print l,l-i,str[i]
		if str[i]!=str[l-1-i]:
			return False
	return True


assert(isPalin('abcba')==True)
assert(isPalin('abcddcba')==True)
assert(isPalin('abcdccba')==False)
