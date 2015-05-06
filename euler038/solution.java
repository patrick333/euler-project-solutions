//Pandigital multiples


public static void main(String[] args) {
		long maxNum = 0;

		long temp;
		long num;
		for (int i = 1; i <= 9; i++) {
			num = 0;
			System.out.printf("%d: ", i);
			for (int j = 1; j <= 5; j++)
				num = Helper.concatenate(num, (long)(i * j));
			System.out.printf("%d ", num);

			for (int j = 6; j <= 9; j++) {
				temp = i * j;
				if (Helper.nOfDigits(num) + Helper.nOfDigits(temp) > 9)
					break;

				num = Helper.concatenate(num, temp);
				System.out.printf("%d ", num);
				if (Helper.nOfDigits(num) < 9) {
					continue;
				} else if (Helper.nOfDigits(num) == 9) {
					if (Helper.isPandigital(num)) {
						System.out.printf("(%d) ", num);
						if (num > maxNum)
							maxNum = num;
					}
				} else
					break;
			}
		}
		System.out.printf("\n");

		for (int i = 10; i <= 99; i++) {// j=4
			num = 0;
			for (int j = 1; j <= 4; j++) {
				num = Helper.concatenate(num, i * j);
			}
			System.out.printf("%d ", num);

			if (Helper.nOfDigits(num)> 9){
				System.out.printf("n(%d)>9, will break out ", num);
				break;
			}
			else if(Helper.nOfDigits(num)< 9)
				continue;
			else {
				if (Helper.isPandigital(num)) {
					System.out.printf("(%d) ", num);
					if (num > maxNum)
						maxNum = num;
				}
			} 
		}
		System.out.printf("\n");

		for (int i = 100; i <= 999; i++) {// j=3
			num = 0;
			for (int j = 1; j <= 3; j++) {
				num = Helper.concatenate(num, i * j);
			}
			System.out.printf("%d ", num);
			
			if (Helper.nOfDigits(num)> 9){
				System.out.printf("n(%d)>9, will break out ", num);
				break;
			}
			else if(Helper.nOfDigits(num)< 9)
				continue;
			else {
				if (Helper.isPandigital(num)) {
					System.out.printf("(%d) ", num);
					if (num > maxNum)
						maxNum = num;
				}
			}
		}
		System.out.printf("\n");

		for (int i = 1000; i <= 9999; i++) {// j=2
			num = 0;
			for (int j = 1; j <= 2; j++) {
				num = Helper.concatenate(num, i * j);
			}
			System.out.printf("%d ", num);
			
			if (Helper.nOfDigits(num)> 9){
				System.out.printf("n(%d)>9, will break out ", num);
				break;
			}
			else if(Helper.nOfDigits(num)< 9)
				continue;
			else {
				if (Helper.isPandigital(num)) {
					System.out.printf("(%d) ", num);
					if (num > maxNum)
						maxNum = num;
				}
			}
		}

		System.out.printf("\nThe max is %d.", maxNum);
	}
//some methods such as concatenate() have been modified to support long data types.