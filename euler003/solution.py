#!/usr/bin/python
# Largest prime factor

import sys
sys.path.append("../common_py")
from prime import *

def main():
	i=3
	N=600851475143
	while True:
		if N%i==0 and isPrime(i):
			N=N/i
			print N
			if isPrime(N):
				break
		i=i+2
	print N



main()	