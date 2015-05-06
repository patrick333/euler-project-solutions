#Coded triangle numbers


def main 
  intArray=[]
  File.open("words.txt", "rb") do |aFile|
    contents=aFile.read
	nameArray=contents.split(",")	#"A""ABILITY""ABLE"...
	intArray=nameArray.map{|x|Helper.sumPOfString(x.delete "\"")}
  end
  
  max=0  #->192
  nMax=0
  intArray.each do |x|
    if x>max
	  max=x
	end  
  end
  nMax=20 #19 is not enough
  
  count=0
  intArray.sort!
  maxJ=intArray.length-1
  triArray=*(1..nMax)
  #puts triArray
  triArray.map!{|x| x*(x+1)/2}

  i=0
  j=0
  if triArray[0]<intArray[0]
	puts "ok"
  end
  while j<=maxJ
    puts "#{triArray[i]}:#{intArray[j]}"
    if triArray[i]>intArray[j]   then# false, and nil are of boolean value "false".
	  j+=1
	elsif   triArray[i]==intArray[j]
      j+=1
	  count+=1
	else
      i+=1	
	end  
  end 

  puts count  
end

main()


