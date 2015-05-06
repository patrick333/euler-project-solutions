
//Pentagon numbers
//1.本题还缺少一个证明:为什么结果是最小的. 为什么不可能有比它更小的了?
//2. 多用断点进行调试；不要用print, printf,etc了！

	public static void generatePenta(int[] penta) {
		for (int i = 0; i <= penta.length - 1; i++) {
			penta[i] = (i + 1) * (3 * i + 2) / 2;
		}
	}
	
	public static boolean isSquare(int t) {
		int n = (int) Math.round(Math.sqrt(t));

		if (n * n == t)
			return true;
		else
			return false;
	}

	public static boolean isPenta(int n) {
		int t = 24 * n + 1;
		// System.out.printf("%d, %d \n", n,t);
		if (!isSquare(t)) {
			// System.out.printf(" %d is not square.",t);
			return false;
		} else {
			t = (int) Math.sqrt(t);
			if ((t + 1) % 6 == 0)
				return true;
			else
				return false;
		}
	}

	public static void main(String[] args) {
		int max = 5000;
		int[] penta = new int[max];
		generatePenta(penta); // penta[0->max-1] are valid.

		// for(int i=0;i<max;i++){
		// // System.out.print(penta[i]);//no display. Too much->not displaying
		// at all!!!
		// System.out.println(penta[i]); //display correctly.
		// }

		int sum = 0;
		int dif = 0;
		for (int i = 0; i < max - 2; i++) {
			for (int j = i + 1; j < max - 1; j++) {
				sum = penta[i] + penta[j];
				dif = penta[j] - penta[i];
				if (isPenta(sum) && isPenta(dif)) {
					System.out.printf("%d,%d: %d,%d->%d,%d\n", i, j, penta[i],
							penta[j], sum, dif);
					// if(dif<min){
					// min=dif;
					// // System.out.printf("%d,%d: %d,%d->%d,%d\n",
					// i,j,penta[i], penta[j],sum, dif);
					// }
				}
			}
		}
	}

