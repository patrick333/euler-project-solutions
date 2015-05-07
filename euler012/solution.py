#Highly divisible triangular number
from math import sqrt,floor
def getNum(N):
    num=1;
    for i in range(2, (int)(sqrt(N)) +1):
        numTemp=0
        while not N%i:
        #    print ""N%i"", N%i
            numTemp=numTemp+1
            N=N/i
        if numTemp:
            num=num*(numTemp+1)
        #print 'i=', i, ':',numTemp, num, N
    if N !=1:
        num*=2;
    return num
num=0
sum=0
i=1
while True:
    sum+=i
    i+=1
    num=getNum(sum)
    #print num
    if num>500:
        break
print sum
