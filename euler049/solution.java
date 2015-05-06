public static long concatenate(int i, int j, int k) {
		long result = k;
		result += (long) j * 10000;
		result += (long) i * 10000 * 10000;
		return result;
	}

	public static boolean arePermutations(int i, int j, int k) {// i<j<k
		int[] digitsI = new int[4];
		int[] digitsJ = new int[4];
		int[] digitsK = new int[4];
		int temp;
		int power;
		temp = i;
		for (int n = 0; n < 4; n++) {
			power = (int) Math.pow(10, 3 - n);
			digitsI[n] = temp / power;
			temp %= power;
		}
		temp = j;
		for (int n = 0; n < 4; n++) {
			power = (int) Math.pow(10, 3 - n);
			digitsJ[n] = temp / power;
			temp %= power;
		}
		temp = k;
		for (int n = 0; n < 4; n++) {
			power = (int) Math.pow(10, 3 - n);
			digitsK[n] = temp / power;
			temp %= power;
		}

		Arrays.sort(digitsI);
		Arrays.sort(digitsJ);
		Arrays.sort(digitsK);
		if (Arrays.equals(digitsI, digitsJ) && Arrays.equals(digitsJ, digitsK))
			return true;
		else
			return false;
	}

	public static void main(String[] args) {

		assert arePermutations(1487, 4817, 8147);
		assert !arePermutations(1487, 4817, 8247);

		int p;
		for (int n = 1001; n < 9999; n += 2) {
			if (!Helper.isPrime(n))
				continue;
			for (int m = n + 2; m <= 9999; m += 2) {
				p = 2 * m - n;
				if (!Helper.isPrime(m) || !Helper.isPrime(p))
					continue;
				else // all prime
				{
					if (arePermutations(n, m, p) && n != 1487) {
						System.out.printf("%d,%d, %d. The num is %d", n,m,p,concatenate(n, m, p));
						break;
					}
				}
			}
		}
	}