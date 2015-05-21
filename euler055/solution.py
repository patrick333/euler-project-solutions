#!/usr/bin/python
#Lychrel numbers
import sys
sys.path.append("../common_py")
from palindrome import *

def isLychrel(d):
	itera=0
	while True:
		itera+=1
		d=d+int(str(d)[::-1])
		if isPalin(str(d)):
			return False
		if itera>=50:
			return True

assert(isLychrel(195)==False)
assert(isLychrel(196)==True)
assert(isLychrel(4994)==True)

def main():
	count=0
	for i in range(196,10000):
		if isLychrel(i):
			count+=1
	print count

main()