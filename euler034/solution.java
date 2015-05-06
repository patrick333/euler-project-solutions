//Digit factorials


public static int factorial(int n){
		if(n==0)return 1;
		else {
			int res=1;
			for(int i=1;i<=n;i++){
				res*=i;
			}
			return res;
		}
	}
	
	public static void main(String[] args) {
		int result=0;
		int[] fac=new int[10]; 
		for(int i=0;i<=9;i++){
			fac[i]=factorial(i);
		}
		for(int n=10; n<=2540160;n++){
			int sum=0;
			int temp=n;
			int r=0;
			while(temp!=0){
				r=temp%10;
				temp/=10;
				sum+=fac[r];
			}
			
			if(n==sum){
				result+=n;
				System.out.printf("%d ", n);
			}
		}
		
		System.out.printf("The result is %d.", result);
	}