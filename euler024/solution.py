#!/usr/bin/python
#Lexicographic permutations

# THIS IS CHEATING TO USE permutations from python!
import itertools
def main():
	pers=list(itertools.permutations(range(10)))
	print pers[999999]


main()