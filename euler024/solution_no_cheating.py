#!/usr/bin/python
#Lexicographic permutations

import sys
sys.path.append("../common_py")
from permutation import *

def main():
	# n=100
	n=1000000
	li=[0,1,2,3,4,5,6,7,8,9];
	for i in range(1,n):
		li=nextPer(li)
		# print li
	print li


main()