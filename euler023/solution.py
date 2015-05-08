#!/usr/bin/python
#Non-abundant sums

def main():
	#find the abundant numbers in [1,28123)
	abun=[]  #use [] or list() to create a list/array
	for i in range(1, 28123):
		sum=0
		for j in range(2,i/2+1):
			if i%j==0:
				sum=sum+j
		if sum>i:
			abun.append(i)
	# print abun

	#mark numbers that can be expressed by the sum
	mark=[False]*28123
	#i<=j
	l=len(abun)
	for i in range(0,l):
		for j in range(i,l):
			if abun[i]+abun[j]<=28123:
				mark[abun[i]+abun[j]-1]=True


	result=0
	for i in range(0,28123):
		if mark[i]==False:
			result=result+i+1
	print result

main()
