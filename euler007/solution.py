#!/usr/bin/python
#10001st prime

import sys
sys.path.append("../common_py")
from prime import *


def main():
	N=3
	i=2
	while True:
		oldN=N
		oldI=i
		if isPrime(N):
			i=i+1
			print oldI, oldN
		N=N+2
		if i>10001:
			break


main()
