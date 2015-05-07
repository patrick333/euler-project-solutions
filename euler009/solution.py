#!/usr/bin/python
#Special Pythagorean triplet


def main():
	for a in range(1,333):
		for b in range(a+1,500):
			if b>=1000-a-b:
				continue
			# print a,b,(1000-a-b)
			if a*a+b*b==(1000-a-b)*(1000-a-b):
				print a,b,a*b*(1000-a-b)
				break

main()	