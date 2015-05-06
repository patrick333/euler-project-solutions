//Double-base palindromes

public static void main(String[] args) {
//		System.out.printf("%b %b\n", Helper.isPalindrome(345), Helper.isPalindrome(91019));
//		System.out.printf("%b %b", Helper.isPalindromeBin(5), Helper.isPalindromeBin(13));
		
		int sum=0;
		for(int n=1; n<1000000;n++){
			if(Helper.isPalindrome(n) && Helper.isPalindromeBin(n)){
				System.out.printf("%d ", n);
				sum+=n;
			}
		}
		
		System.out.printf("\nThe number is %d.", sum);
	}

	public static int nOfDigitsBin(int n){
		int temp=n;
		int count=0;
		while(temp!=0){
			temp/=2;
			count++;
		}		
		return count;
	}

	public static boolean isPalindrome(int n){
		assert n>=0;
		if(n/10==0)return true; //0->9
		else {
			int c=nOfDigits(n);
			int[] digits=new int[c];
			int temp=n;
			for(int i=0;i<c;i++){
				digits[i]=temp%10;
				temp/=10;
			}
			
			for(int i=0;i<c/2;i++){
				if(digits[i]!=digits[c-1-i])
					return false;
			}
			return true;
		}
	}
	
	public static boolean isPalindromeBin(int n){
		assert n>=0;
		if(n<=1)return true;
		else {
			int c=nOfDigitsBin(n);
			int[] digits=new int[c];
			int temp=n;
			for(int i=0;i<c;i++){
				digits[i]=temp%2;
				temp/=2;
			}
			
			for(int i=0;i<c/2;i++){
				if(digits[i]!=digits[c-1-i])
					return false;
			}
			return true;
		}	
	}
