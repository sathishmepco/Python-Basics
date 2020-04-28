#include <iostream>
using namespace std;

int main()
{
	int array1[] = {2,4,3,5,1,6,8,32};
	int array2[] = {3,4,5,9,10,6,12};
	int n1 = sizeof(array1)/sizeof(int);
	int n2 = sizeof(array2)/sizeof(int);
	int outputSize = 0;
	if( n1 < n2)
	    outputSize = n1;
	else
	    outputSize = n2;
	  
	int output[outputSize];
	int outputIndex = 0;
	for(int i=0;i<n1;i++){
        for(int j=0;j<n2;j++){
        	if(array1[i] == array2[j]){
        		output[outputIndex] = array1[i];
        		outputIndex++;
        		break;
        	}
        }
    }
	
	for(int i=0;i<outputIndex;i++)
		cout<<output[i]<<"-";
	return 0;
}