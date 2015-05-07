//Largest palindrome product

bool palin(int n){ //n has 5 or 6 digits.
	int digits[6];
	bool re=false;
	for(int i=0; i<6;i++){
		digits[i]=(n / (int) pow( (float)10,i)) %10;
		//cout<<""digits[""<<i<<""] is ""<<digits[i]<<endl;
	}
	if(digits[5]==0){
		if(digits[4]==digits[0] &&digits[3]==digits[1] )
			re=true;
	}
	else {
		if(digits[5]==digits[0] &&digits[4]==digits[1] && digits[3]==digits[2] )
			re=true;
	}
	return re;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	int max=0;
	for(int i=100; i<=999; i++){
		for(int j=i; j<=999; j++)
		{
			n=i*j;
			//printf(""i=%d, j=%d, n=%d \n"", i,j,n);
			if(palin(n) && n>max)
				max=n;
		}
	}
	if(max>0)
		cout<<""the largest palindrome is ""<<max<<endl;
	return 0;
}