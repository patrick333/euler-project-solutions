#Pandigital prime


def main #"Everyone knows Ruby is slow. " but this main1 is too slow.
  max=0
  (1001..999999999).step(2) do |x|
  #(1001..999999).step(2) do |x|
    if Helper.isPrime(x) && Helper.isPandigital(x)
	  max=x
	  print "#{x} "
	end  
  end
  return max
end



def main2
  m=["7654321","4321"]  #use [], same as python's list; not the same as c++,c#'s array.
  i=0
  while i<=1
    n=m[i]
    puts "Initially, n is #{n}"
	k=0
	l=0
	if(Helper.isPrime(Integer(n)))
	  print "Initially, n is prime"
	  return n
	end
	
	while !Helper.isMinInPandigitalS(n)
	  (0..(n.length-2)).each do |ii| 
	    if Integer(n[ii])>Integer(n[ii+1])
	      k=ii
	    end
	  end
	
	  ((k+1)..(n.length-1)).each do |ii| 
	    if Integer(n[k])>Integer(n[ii])
	      l=ii
	    end
      end
	  puts "#{k},#{l} "	
	
	  #swap, and reverse
	  n[k], n[l]=n[l],n[k]
	  n=Helper.reverseSubS(n,k+1,n.length-1)
	  if(Helper.isPrime(Integer(n)))
	    print "After switching, n is prime. "
        return n
	  end	
	  #puts n
	end  
	
  i-=1;
  end
end