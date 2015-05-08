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

def sieve(limit):
	nums = range(limit+1)
	nums[1] = 0

	for n in nums:
	    if n:
	        for x in range(2*n, limit+1, n):
	            nums[x] = 0 # counting this vs. pop
	# print nums
	# print filter(None, nums)
	return set(filter(None, nums))

# print sieve(100)



