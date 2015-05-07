#!/usr/bin/python
# Largest palindrome product


def palin(n): 
	digits=[] 
	re=False 
	for i in range(0,6): 
		digits. append( (n/ pow(10, i) )%10) 
	if digits[5]==0: 
		if digits[4]==digits[0] and digits[3]==digits[1]: 
			re=True; 
	else: 
		if digits[5]==digits[0] and digits[4]==digits[1] and digits[3]==digits[2]: 
			re=True 
	return re 

def main():
	n=0 
	max=0 
	for i in range(100, 1000): 
		for j in range(i, 1000): 
			n=i*j 
			if palin(n) and n>max: 
				max=n 
	if max>0: 
		print "the largest palindrome is ", max

main()