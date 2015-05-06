

#Ruby doesn't require us to use any character to separate commands, 
#unless we want to chain multiple statements together on a single line. 
def offDigit(o,j) 
	temp=j
	r=0
	for i in 0..o
		r=temp%10
		temp/=10
	end
	return r
end

def digitAtPosition(p)
	dCount = 0;
	j=1;
	while true
		if j<=9 #then is optional
			dCount += 1
		elsif j <= 99
			dCount += 2
		elsif j <= 999
			dCount += 3
		elsif j <= 9999
			dCount += 4
		elsif j <= 99999
			dCount += 5
		elsif j <= 999999
			dCount += 6	
		else 
			dCount += 7
		end		
		if(dCount>=p)	
		  return offDigit(dCount-p,j);
		end  
		j+=1
	end		
end

product = 1
product*=digitAtPosition(1)
product*=digitAtPosition(10)
product*=digitAtPosition(100)
product*=digitAtPosition(1000)
product*=digitAtPosition(10000)
product*=digitAtPosition(100000)
product*=digitAtPosition(1000000)

puts "\nThe product is #{product}"