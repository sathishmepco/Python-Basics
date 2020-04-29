//Find the x & y where z = x+y, z is given input
int main(){
	int array[] = {4, 5, 2, 3, 6, 9};
	int n = sizeof(array) / sizeof(int);
	int Z = 14;
	int flag = 0;
	int i,j;
	for(i=0;i<n-1;i++){
		for(j=i+1;j<n;j++){
			if(array[i] + array[j] ==Z){
				cout<<array[i]<<" "<<array[j];
				flag = 1;
				break; // gives only one solution
			}
		}
	}
	if(x==0 && y==0)
		cout<<"DOES NOT EXIST";		
	return 0;
}
/*

*/