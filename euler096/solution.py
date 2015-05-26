#!/usr/bin/python
#Su Doku


#algo: http://norvig.com/sudoku.html

def solveAGrid(grid):






def main():
	lines=open('sudoku.txt',"r").read().splitlines()
	l=len(lines)
	grids=[[[0 for i in xrange(9)] for j in xrange(9)] for k in xrange(50)]
	# print grids
	# assert(l==500)
	i=0
	for line in lines:
		d=i/10
		if i%10!=0:
			grids[d][(i-1)%9]=[int(x) for x in list(line)]
			# print grids[d][(i-1)%9]
		i+=1

	solveAGrid(grids[0])






main()