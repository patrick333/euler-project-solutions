#Longest Collatz sequence


max=1

iMax=1

maxN=1000000

#maxN=30

for i in range(1, maxN):

    j=i

    len=1

    while j!=1:

        if j%2==0:

            j=j/2

        else:

            j=3*j+1

        len+=1

    if(len>max):

        max=len 

        iMax=i

    #print i, len

print iMax, max