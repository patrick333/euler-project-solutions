#!/usr/bin/python
#Square root convergents



def main():
	itera=1
	numerator=1
	denominator=1
	count=0
	while True:
		temp=2*denominator+numerator
		denominator=denominator+numerator
		numerator=temp


		if len(str(numerator))>len(str(denominator)):
			count+=1
		if itera>1000:
			break
		itera+=1
	print count


main()