#include <iostream>
#include <math.h>
#include <cstring>

using namespace std;

int main()
{
    string s = "";   //input  1010
	cin>>s;
	int n = s.size();	//4
	int decimal = 0; //output
	int powerIndex = 0;
	for(int i=n-1; i>=0; i--){
		if(s[i] == '1'){ //1
			decimal = decimal + 1 * pow(2,powerIndex);
		}
		powerIndex++;
	}
	cout<<"Decimal value is : "<<decimal;
	return 0;
}
