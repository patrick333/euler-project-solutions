//Integer right triangles

public static void main(String[] args) {
		int theP=0 ;

		int maxCount=0;
		int count;
		int c;
		for(int p=12;p<=1000;p+=2)		{//p must be even
			count=0;
			System.out.printf("%d:", p);
			for(int a=1; a<=p/3; a++){
				for(int b=p/3; b<=p/2; b++){
					c=p-a-b;
					if(a*a+b*b==c*c){
						count++;
						System.out.printf("(%d, %d, %d) ", a,b,c);
					}
				}
			}
			if(count>maxCount){
				maxCount=count;
				theP=p;
			}
			System.out.printf("\n");
		}

		System.out.printf("\nThe perfect p is %d.", theP);
	}