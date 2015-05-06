//Digit canceling fractions


public static void main(String[] args) {	
		int numerator=1;
		int denominator=1;
		
		//for the type ax/bx=a/b
		int count=0;
		for(int a=1;a<9;a++){
			for(int b=a+1;b<=9;b++){				
				if( (9*a*b)%(10*a-b)==0){
					int x1=(9*a*b)/(10*a-b);
					if(x1<=9&&x1>=1){
						count++;
						numerator*=a;
						denominator*=b;
					}
				}				
				else if( (9*a*b)%(10*b-a)==0){
					int x2=(9*a*b)/(10*b-b);
					if(x2<=9&&x2>=1){
						count++;
						numerator*=a;
						denominator*=b;
					}
				}
			}//end of inner for.
		}
		
		System.out.printf("Found %d such fractions. The product is %d/%d",count,numerator,denominator   );//printf=format.		
	}
