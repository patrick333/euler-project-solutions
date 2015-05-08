#!/usr/bin/python
#1000-digit Fibonacci number

from math import log
def nOfDigits(N):
	return int((log(N+1,10))+1)

def main():
	a=1
	b=1
	i=3
	n=1000
	# n=6
	while True:
		temp=b
		b=a+b
		a=temp
		if nOfDigits(a)>=n:
			print i,a
			break
		# print i,a
		i+=1




main()