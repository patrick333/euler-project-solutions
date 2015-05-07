//Largest prime factor
bool prime(long long d){
	if(d==2)return true;
	else if(d%2==0) return false;
	else {
		for(int i=3;i<=floor(sqrt((double)d)) ;i+=2){
			if(d%i==0)
				return false;
		}
		return true;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	//int num=210;
	long long num=600851475143 ;
	for(int i=3;;i+=2){
		printf(""i=%d num=%d \n"", i,num);
		while(num%i==0 && prime(i))
			num=num/i;
		if(prime(num))break;
	}
	printf(""Largest prime factor is %d \n"", num);
	return 0;
}