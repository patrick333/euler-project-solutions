public static int offDigit(int o, int j) {
		int temp = j;
		int r=0;
		for (int i = 0; i <= o; i++) {
			r = temp % 10;
			temp /= 10;
		}		
		return r;
	}

	public static int digitAtPosition(int p) {
		int dCount = 0;
		for (int j = 1; ; j++) {//j <= 9999999
			if (j <= 9)
				dCount += 1;
			else if (j <= 99)
				dCount += 2;
			else if (j <= 999)
				dCount += 3;
			else if (j <= 9999)
				dCount += 4;
			else if (j <= 99999)
				dCount += 5;
			else if (j <= 999999)
				dCount += 6;
			else
				// j<=9999999)
				dCount += 7;

			if (dCount >= p) {
				System.out.printf("j=%d, dCount=%d, p=%d. digit=%d\n", j, dCount,p, offDigit(dCount-p,j));
				return offDigit(dCount-p,j);
			}
			else 
				continue;
		}
	}

	public static void main(String[] args) {		
		int product = 1;
		product*=digitAtPosition(1); 
		product*=digitAtPosition(10);
		product*=digitAtPosition(100);
		product*=digitAtPosition(1000);
		product*=digitAtPosition(10000);
		product*=digitAtPosition(100000);
		product*=digitAtPosition(1000000);
		
		System.out.printf("\nThe product is %d.", product);
	}