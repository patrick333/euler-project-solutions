#!/usr/bin/python
#Powerful digit sum

def main():
	maxSum=0
	for i in range(1,100):
		for j in range(1,100):
			string=str(pow(i,j))
			tempSum=sum([int(x) for x in string ])
			if tempSum>maxSum:
				maxSum=tempSum

	print maxSum




main()