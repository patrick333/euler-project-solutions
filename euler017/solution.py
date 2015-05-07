#Number letter counts
def numW(N):
    num=0
    num1=[3,3,5,4,4,  3,5,5,4,3]
    num15=[6,6,8,8,7,  7,9,8,8]
    num2=[3,6,6,5,5,  5,7,6,6]
    if N==0:
        num=0
    elif N<=10:
        num=num1[N-1]
    elif N<20:
        num=num15[N-11]
    elif N<100:
        num=num2[N/10-1]+numW((int) (N%10) )
    elif N<1000:
        num=num1[N/100-1]+7+ numW((int)(N%100))
        if N%100!=0:
            num+=3
    else: #N=1000
        num=11
    return num    

print numW(999), numW(19),numW(342), numW(115),numW(10),numW(200)
print numW(201), numW(20)
sum=0

for i in range(1,1001):
    sum+=numW(i)
print sum     
print range(10)
