#include <iostream>
using namespace std;

int main()
{
int array[] = {4, 5, 2, 3, 6, 9};
	int n = sizeof(array) / sizeof(int);
	int Z = 4;
	
	//sorting 
	for(int i=0;i<n-1;i++)
		for(int j=i+1;j<n;j++)
			if(array[i] > array[j]){
				int temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}

    int i,j;
	i=0;
	j=n-1;
	
	while(i < j){
		int sum = array[i] + array[j];
		if(sum == Z){
			cout<<"X,Y are found!"<<endl;
			cout<<array[i]<<" "<<array[j];
			return 0;
		}else if (sum < Z)
			i++;
		else if(sum > Z)
			j--;
	}
	cout<<"DOES NOT EXIST!";
	return 0;
}

/*
X,Y are found!
2 6    
*/