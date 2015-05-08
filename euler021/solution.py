#!/usr/bin/python
#Amicable numbers
from math import *

def d(n):
	sum=0
	for i in range(1,n/2+1):
		if n%i==0:
			sum=sum+i
	return sum

def main():
	#suppose a<b
	result=0
	for a in range(2,10000):
		b=d(a)
		if b<=a or b>=10000:
			continue
		if a==d(b):
			result=result+a+b
			print a,b,result
	print result

main()

