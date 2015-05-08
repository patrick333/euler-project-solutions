#!/usr/bin/python

#li is a list, such as [1,2,3]
#algo: 
#1. search from right to left, find the first i such that li[i-1]<li[i]
#2. search again from li[n-1] to li[i], to find the first k such that li[k]>li[i-1]
#3. switch li[k] and li[i-1]
#4. reverse li[i~n-1]
def nextPer(li):
	l=len(li)
	for i in range(l-1,0,-1):
		if li[i-1]<li[i]:
			# print i
			for k in range(l-1,i-1,-1):
				if li[k]>li[i-1]:
					#switch:
					temp=li[k]
					li[k]=li[i-1]
					li[i-1]=temp
					# print li
					break

			#reverse:
			numOfSwitches=(l-i)/2
			for m in range(i,i+numOfSwitches):
				temp=li[m]
				li[m]=li[l-1+i-m]
				li[l-1+i-m]=temp
			break


	return li


# #test:
# li=[0,1,2,4]
# for i in range(4*3*2*1-1):
# 	li=nextPer(li)
# 	print li



