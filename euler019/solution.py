#Counting Sundays
def leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False
            
def d(y,m):#how many days for this month
    if m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2:
        if leap(y):
            return 29
        else:
            return 28
    else:
        return 31
 
Day=[[] for _ in range(101)]
for i in range(101):
    Day[i]=[0,0,0,0,0,0,0,0,0,0,0,0]
#0 for sunday, 1 for monday, etc.     
#print Day
       
num=0      
for y in range(1900, 2001):    
#for y in range(1900, 1921):
    for m in range(1,13):
        
        if y==1900 and m==1: #january 1       
            Day[y-1900][m-1]=1
        else:
            if m==1: #january 1
                Day[y-1900][0]=(d(y-1,12)+Day[y-1901][11])%7
            else:
                Day[y-1900][m-1]=(d(y,m-1)+Day[y-1900][m-2])%7
        print 'y=',y, ' m=', m, ' Day[y-1990][m-1]=',Day[y-1900][m-1]      
        if y>=1901 and Day[y-1900][m-1]==0:
            num+=1
print num  
