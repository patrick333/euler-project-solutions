#!/usr/bin/python
#Spiral primes

import sys
sys.path.append("../common_py")
from prime import *

def getNumOfNewPrimesForItera(i):
	lastN=(2*i-1)**2
	l=2*i
	a=lastN+l
	b=a+l
	c=b+l
	d=c+l
	count=0
	if isPrime(a):
		count+=1
	if isPrime(b):
		count+=1	
	if isPrime(c):
		count+=1
	if isPrime(d):
		count+=1
	# print lastN,l, a,b,c,d,count
	return count	

def main():
	itera=0
	count=0 #num of primes
	#2*itera+1
	while True:
		itera+=1
		count+=getNumOfNewPrimesForItera(itera)

		
		# if count< 0.32*(4*itera+1):
		if count< 0.1*(4*itera+1):	
			print 2*itera+1
			break

# assert(getNumOfNewPrimesForItera(1)==3)
# assert(getNumOfNewPrimesForItera(2)==2)
# assert(getNumOfNewPrimesForItera(3)==3)
main()