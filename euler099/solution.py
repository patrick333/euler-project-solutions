#!/usr/bin/python
#Largest exponential

from math import log10
def main():
    lines = open('base_exp.txt',"r").read().splitlines()
    l=len(lines)
    maxIndex=-1
    maxValue=0
    for i in range(0,l):
        base,exp=lines[i].split(',');
        temp=float(exp)*log10(float(base))
        if temp>maxValue:
            maxValue=temp
            maxIndex=i+1
    print maxIndex




main()