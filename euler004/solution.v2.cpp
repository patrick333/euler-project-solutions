//an improvement
bool palin(int n){ //n has 5 or 6 digits.
	int digits[6];
	int temp=n;
	bool re=false;
	for(int i=0; i<6;i++){
		digits[i]=temp%10;
		temp=temp/10;
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