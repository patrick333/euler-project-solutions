//Consecutive prime sum


public static void main(String[] args) {
	int limitP = 1000000;
	ArrayList<Integer> listPrimes = new ArrayList<Integer>();
	listPrimes.add(2);
	for (int i = 3; i < limitP; i += 2) {
		if (Helper.isPrime(i))
			listPrimes.add(i);
	}
	Integer[] primes = new Integer[listPrimes.size()];
		primes = listPrimes.toArray(primes); 
		int numP = primes.length;

		int maxNumConP = 2;
		int theSum = 0;
		int tempSum;
		for (int i = 0; i < numP; i++) {
			tempSum = primes[i];
			for (int j = i + 1; j < numP; j++) {
				tempSum += primes[j];
				if (tempSum >= limitP)
					break;
				else if (j - i + 1 > maxNumConP && Helper.isPrime(tempSum)) {
					maxNumConP = j - i + 1;
					theSum = tempSum;
				} else {
				}
			}
		}

		System.out.printf("Sum is %d", theSum);
	}










