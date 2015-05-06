//Distinct primes factors




// 此例用到java assertions. 并大量使用了breakpoins.
	public static boolean hasFourPrimeDivisor(long l){
		int count=0;
		long temp=l;

		long i=2;
		boolean isUsedI;
		while(i<=(long)Math.floor(Math.sqrt(temp)) && temp>=i ){
			isUsedI=false;
			while(temp%i==0){
				temp/=i;
				if(!isUsedI&&Helper.isPrime(i)){
					count++;
					isUsedI=true;
				}
			}
			i++;
		}
		
		if(Helper.isPrime(temp))
			count++;
		
		if(count>=4)
			return true;
		else 
			return false;
	}
	

	public static void main(String[] args) {
		assert !hasFourPrimeDivisor(264);
		assert hasFourPrimeDivisor(330);
		
		
		boolean a;
		boolean b;
		boolean c;
		boolean d;
		for(long i=644;;i++){
			a=hasFourPrimeDivisor(i);
			b=hasFourPrimeDivisor(i+1);
			c=hasFourPrimeDivisor(i+2);
			d=hasFourPrimeDivisor(i+3);
			if(a&&b&&c&&d){
//				System.out.printf("The num is %ld", i); //format is not exactly the same as in c/c++.
				System.out.printf("The num is %d", i);
				break;
			}
						
		}//end of for. 
	}


