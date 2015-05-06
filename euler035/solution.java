//Circular primes

public static void main(String[] args) {
		int count=4;
		for(int n=11; n<1000000;n++){
			if(Helper.isCirPrime(n)){
				count++;
				System.out.printf("%d ", n);
			}
		}
		
		System.out.printf("The number is %d.", count);
	}

public class Helper {

	
	public static boolean isPrime(int n){
		assert n>=2;
		if(n==2)return true;
		else if(n%2==0){
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
	
	public static int nOfDigits(int n){
		int temp=n;
		int count=0;
		while(temp!=0){
			temp/=10;
			count++;
		}		
		return count;
	}
	
	public static int nextNumberCirular(int n, int c){
		int power=(int)Math.pow(10.0, c-1);
		int topDigit=n/power;
		int rest=n-topDigit*power;
		return topDigit+10*rest;
	}
	
	public static boolean isCirPrime(int n){
		assert n>=11;
		if(!isPrime(n))
			return false;
		
		int c=nOfDigits(n);
		int temp=n;
		for(int i=c-1;i>=1;i--){
			temp=nextNumberCirular(temp,c);
//			System.out.printf("n=%d, c=%d, temp=%d ", n,c,temp);
			if(!isPrime(temp))
				return false;
		}
		return true;
	}
}



