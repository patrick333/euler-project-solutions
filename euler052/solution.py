#!/usr/bin/python
#Permuted multiples

def getDigits(N):
	return sorted(str(N))


def main():
	n=9999
	while not getDigits(2*n)==getDigits(3*n)==getDigits(4*n)==getDigits(5*n)==getDigits(6*n):
		n+=9
	print n

# print getDigits(194967)
main()