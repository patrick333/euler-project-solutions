#!/usr/bin/python
#Summation of primes

import sys
sys.path.append("../common_py")
from prime import *

def main():
	num=2000000
	sum=2

	for i in range(3, num,2):
		if isPrime(i):
			sum=sum+i
	print sum

main()