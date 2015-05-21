#!/usr/bin/python
#Powerful digit counts

from math import pow,ceil
def main():
	count=0
	n=1
	lowerBound=0
	while lowerBound<=9:
		lowerBound=ceil(pow(10,(n-1)/(1.0*n)  ) )
		print lowerBound
		count+=10-lowerBound
		n+=1
	print count


main()