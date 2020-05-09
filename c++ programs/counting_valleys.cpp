int main(){
	char carr[] = "DUDUDDUU";
	int n = sizeof(carr) / sizeof(char);
	int steps = 0;
	int valleyCounter = 0;
	for(int i=0;i<n;i++){
		if(carr[i] == 'U')
			steps++;
		else if(carr[i] == 'D')
			steps--;
		if(steps == 0 && carr[i] == 'U')
			valleyCounter++;
	}
	cout<<valleyCounter;
	return 0;
}