//Truncatable primes



public static boolean isTruncPrime(int n){
		int c=Helper.nOfDigits(n);
		int temp=n;
		if(!Helper.isPrime(n))
			return false;
		else{
//			System.out.printf("%d: ",n);
			while(temp>10){//right->left
				temp/=10;
//				System.out.printf("%d ",temp);
				if(!Helper.isPrime(temp))
					return false;
			}
			
//			System.out.printf("||");
			temp=n;
			int power;
			int top;
			for(int i=c-1;i>=1;i--){
				power=(int)Math.pow(10.0, i);
				top=temp/power;
				temp=temp-top*power;
//				System.out.printf("%d ",temp);
				if(!Helper.isPrime(temp))
					return false;
			}
		}//end of else
		
		
		return true;
	}

	public static void main(String[] args) {		
		int c=0;
		int sum=0;
		for(int n=11;;n++){
			if(isTruncPrime(n)){
				c++;
				sum+=n;
				System.out.printf("%d:%d ",c,n);
			}
			if(c>=11)
				break;
		}		
		System.out.printf("\nThe number is %d.", sum);
	}
and some changes are in isPrime.
	public static boolean isPrime(int n){//suppose n>=0
//		assert n>=2:"n should be  at least 2";  //need the option -ea
		
		if(n==2)return true;
		else if(n%2==0 || n==1){
			return false;
		}
		else{
			for(int i=3;i<=(int)Math.sqrt(n);i+=2){
				if(n%i==0)
					return false;
			}
		}
		
		return true;
	}