#!/usr/bin/python
#Combinatoric selections

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def main():
    # print nCr(23,10)
    count=0
    for n in range(23,101):
        for r in range(1,n):
            if nCr(n,r)>1000000:
                count+=1
    print count

main()