#!/usr/bin/python
#Totient maximum

#   use this http://en.wikipedia.org/wiki/Euler%27s_totient_function#Example

import sys
sys.path.append("../common_py")
from prime import *

# def phi(n):
# 	factors=[]
# 	while True:

# 	return n


# def main():
# 	maximum=0
# 	for n in range(6,1000001):
# 		if phi(n)>maximum:
# 			maximum=phi(n)
# 	print maximum



def main():
	primes=list(sieve(30))
	primes.sort()  #sorting in-place!!
	# print primes

	result=1
	i=0
	while result*primes[i]<=1000000:
		result*=primes[i]
		i+=1
	print result

main()