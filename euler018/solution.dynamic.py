#!/usr/bin/python
#Maximum path sum I



def main():
	lines = open('triangle.txt',"r").read().splitlines()
	l=len(lines)
	triangles=[]
	for line in lines:
		triangles.append([int(x) for x in line.split()])
	# print triangles
	# print triangles[0][0]+triangles[1][0]

	for i in range(l-2,-1,-1):
		for j in range(0,i+1):
			triangles[i][j]+=max(triangles[i+1][j],triangles[i+1][j+1])
		print triangles[i]
	print triangles[0][0]


main()
