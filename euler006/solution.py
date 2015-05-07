#!/usr/bin/python
#Sum square difference



def main():
	N=0
	for i in range(1, 101):
		for j in range(i+1,101):
			N=N+i*j
	print 2*N




main()