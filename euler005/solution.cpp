//Smallest multiple
int _tmain(int argc, _TCHAR* argv[])
{
	int m[8];
	m[0]=2; 
	m[1]=3;
	m[2]=5;
	m[3]=7;
	m[4]=11;
	m[5]=13;
	m[6]=17;
	m[7]=19;
	int n[8]; //factors for 2, 3, 5,7, 11, 13, 17, 19
	
	for(int i=4; i<=20; i++){
		for(int j=0; j<8; j++){
			int factor=0; 
			int temp=i; 
			while(temp%m[j]==0){  //not while(temp%m[j])!!!!
				factor++;
				temp/=m[j];
			}
			if(factor>n[j])
				n[j]=factor;
		} //for j. 
	}
	
	for(int j=0; j<8; j++){
		printf(""j=%d, base=%d, factor=%d \n"", j, m[j], n[j]);
	}

	int num=1;
	for(int j=0; j<8; j++){
		num=num*(int ) pow( (float)m[j], n[j]);
	}
	cout<<""the smallest mutiple is ""<<num<<endl;
		
	return 0;
}