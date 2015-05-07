#!/usr/bin/python
from math import ceil, sqrt
def isPrime(d):
	if d==2:
		return True
	elif d%2==0:
		return False
	else:
		for i in range(3,int(ceil(sqrt(d))+1),2):
			if d%i==0:
				return False
		return True







