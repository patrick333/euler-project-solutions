#!/usr/bin/python
#Names scores

def scorePerWord(str):
	sum=0
	for a in str:
		sum=sum+ord(a)-ord('A')+1
	return sum


def main():
	f = open("p022_names.txt",'r')
	string = f.read()
	li=string.replace('\"','').split(",");
	li.sort();
	# print li

	score=0
	for element in li:
		score=score+scorePerWord(element)*(li.index(element)+1)

	print score


main()
