#!/usr/bin/python
#Multiples of 3 and 5

def isMultiple(N):
	if N%3==0 or N%5==0:
		return True;
	else:
		return False;

def main():
	result=0
	for i in range(3, 1000):
		if isMultiple(i):
			result=result+i
	print result

main()