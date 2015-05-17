#import <Foundation/Foundation.h>
#import "../common_m/prime.h"



int add (int a, int b)
{
    int c;
    c = a + b;
    return c;
}

int main(int argc, const char * argv[]) {
	@autoreleasepool {
		Prime * prime =[[Prime alloc]init];
		[prime compute];

	// int result=add(3,4);
	// NSLog(@"%d", result);	
	// NSLog(@"Hello, World!");
	}
	return 0;
}