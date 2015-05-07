//10001st prime
int _tmain(int argc, _TCHAR* argv[])
{
	long long num=0;
	int index=0;
	int maxIndex=10001;
	//int maxIndex=10;
	for(long long d=2; ;d++){
		if(prime(d)){
			index++;
			printf(""%d "", d);
			if(index>=maxIndex){
				num=d;
				break;
			}
		}
	}
	cout<<""the 10001st prime is ""<<num<<endl;
	return 0;
}