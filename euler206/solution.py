#!/usr/bin/python
#Concealed Square

#X should have the form of 1....0, with 8 digits in-between.

def digitAt(i,N):
	return (N/pow(10,i))%10


def hasSqureTheForm(n):
	square=pow(n,2)
	return digitAt(0,square)==0 and digitAt(2,square)==9 and digitAt(4,square)==8 and digitAt(6,square)==7\
	and digitAt(8,square)==6 and digitAt(10,square)==5 and digitAt(12,square)==4 and digitAt(14,square)==3 \
	and digitAt(16,square)==2 and digitAt(18,square)==1

def main():
	for n in range(10000000,100000000):
		composeN=pow(10,9)+n*10
		if hasSqureTheForm(composeN):
			print composeN
			break

# print digitAt(3,9423)
# print hasSqureTheForm(90)
main()