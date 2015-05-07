#!/usr/bin/python
#Even Fibonacci numbers

def main():
	a=2
	b=3
	sum=2
	while True:
		temp=a
		if a>4000000:
			break
		else:
			print a,b,sum
			a=a+2*b
			b=temp*2+3*b
			sum=sum+a


main()