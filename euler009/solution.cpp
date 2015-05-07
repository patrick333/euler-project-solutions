//Special Pythagorean triplet
int _tmain(int argc, _TCHAR* argv[])
{
	float limit=1000/ (2+sqrt( (float)2.0));
	printf(""limit=%f \n"", limit);
	int product=0;
	for(int a=1;a<limit; a++){
		for(int b=(int)ceil(limit); b<1000; b++){
			float result=a+b+ sqrt((float) (a*a+b*b)  )- 1000.0;
			if( abs(result)< 1.0e-10  ){
				product=a*b*(1000-a-b);
				printf(""the product is %d \n"", product);
			}
		}
	}
	return 0;
}