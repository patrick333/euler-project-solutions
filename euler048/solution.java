//Self powers


public static long pTen=(long) (Math.pow(10, 10));
	public static long getTenDigits(long l) {
		return l % pTen;
	}

	public static long digitsOfPow(long i) {
		long product=1;
		for (long j = 1; j <= i; j++) {
			product*=i;
			product=getTenDigits(product);
		}

		return product;
	}

	public static void main(String[] args) {

		assert digitsOfPow(11)==5311670611l;
		long sum=0;
		for (long i = 1; i <= 1000; i++) {
			sum+=digitsOfPow(i);
		}
		System.out.printf("Sum is %d", getTenDigits(sum));
	}




