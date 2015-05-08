#!/usr/bin/python
#Prime digit replacements

import sys
sys.path.append("../common_py")
from prime import *
import string

def isPrimeEightFamily(p,digit):
	s=str(p)
	c=0
	for d in str('0123456789'):
		newP=int(str.replace(s,digit,d))
		if isPrime(newP):
			# print newP
			c+=1
	# print c
	return c==8


def main():
	for prime in sieve(1000000):
		li=str(prime)
		if li.count('0')==3 and isPrimeEightFamily(prime,'0') \
		or li.count('1')==3 and isPrimeEightFamily(prime,'1') \
		or li.count('2')==3 and isPrimeEightFamily(prime,'2'):
			print prime




# isPrimeEightFamily(501,'0')
main()