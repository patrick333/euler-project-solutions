//Summation of primes

bool prime(long long d){

	if(d==2)return true;

	else if(d%2==0) return false;

	else {

		for(int i=3;i<=sqrt((double)d)  ;i+=2){

			if(d%i==0)

				return false;

		}

		return true;

	}

}



int _tmain(int argc, _TCHAR* argv[])

{

	long long num=2000000;

	//long long num=200;



	long long sum=2;

	for(long long i=3; i<num; i+=2){

		if(prime(i)){

			//printf(""%d "", i);

			sum+=i;

		}

	}



	printf(""sum=%lld \n"", sum);

	return 0;

}