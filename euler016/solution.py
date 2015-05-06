#Power digit sum

def numDigits(N):

    r=0

    while N:

        r,N=r+N%10, N/10

    return r

    

num=1

for i in range(100):

    num*=1024

print num    

print numDigits(num)

print numDigits(4495)