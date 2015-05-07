#!/usr/bin/python
#Smallest multiple



def main():
	#m[], n[] for bases, and factors. 
	m=[0]*8
	n=[0]*8
	m[0]=2
	m[1]=3
	m[2]=5
	m[3]=7
	m[4]=11
	m[5]=13
	m[6]=17
	m[7]=19

	for i in range(4,21):
		for j in range(0,8):
			factor=0
			temp=i
			while temp%m[j]==0:
				factor=factor+1
				temp=temp/m[j]
			if factor>n[j]:
				n[j]=factor

	N=1
	for j in range(0,8):
		N=N*pow(m[j],n[j])
		print j, m[j],n[j], N

main()