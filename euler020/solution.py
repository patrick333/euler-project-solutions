

from math import factorial



num=factorial(100)         

sumD=0    

while num!=0:

    num,sumD=num/10, sumD+num%10

 

print sumD 