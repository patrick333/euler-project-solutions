


#Ruby too slow, 有例为证 http://www.oschina.net/translate/ruby-is-too-slow-for-programming-competitions
#another reason is that you should operate on numbers instead of strings. "我比较了两个函数的性能，一个先转换为字符串再判断是否是回文，一个使用整数计算来判断是否是回文数，因为我听说计算机做整数计算相当快."	
def goWithProperty(n)
d=[n[1,3],n[2,3],n[3,3],n[4,3],n[5,3],n[6,3],n[7,3]]  # 7 items
#puts d
#delete the first 0 of these numbers, if any
d.each do |x|
  #puts x[0]
  if x[0]=="0"
    x=x[1..(x.length-1)]
	#puts x
  end
end

prime=[2,3,5,7,11,13,17]
(0..6).each do |i|
  #print "#{d[i]} "
  if (d[i].to_i)%prime[i]!=0  #should not use Integer(s); use to_i, to_int, instead
    return false
  end	
end
return true
end

def main 
s="1023456789"
count=0
sum=0
#while !Helper.isMaxInPandigitalS(s)
while s.to_i<9876543210 #after the change, much faster
  if goWithProperty(s)
    count+=1
	sum+=s.to_i
	puts s
  end  
  s=Helper.nextPandigitalS(s)
end 
puts sum
end

main()