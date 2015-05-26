#!/usr/bin/python
#Square digit chains

def squareDigSum(d):
    result=0
    for i in str(d):
        result+=int(i)**2
    return result

# assert(squareDigSum(89)==145);
# assert(squareDigSum(32)==13);

def main():
    count=0
    # maxValue=100
    maxValue=10000000
    search=[0 for i in range(1,1001)];#1 for those ending with 1; 2 for those ending with 89
    search[1]=1
    search[89]=2
    for i in range(1,maxValue):
        # print 'start with ',i
        result=i
        temp=[]
        while True:
            if result<1000:
                if search[result]!=0:
                    for t in temp:
                        search[t]=search[result]
                    if search[result]==2:
                        count+=1
                    # print 'breaking at result=',result
                    break
                temp.append(result)
            result=squareDigSum(result)
            # print result
    print 'count=',count





main()