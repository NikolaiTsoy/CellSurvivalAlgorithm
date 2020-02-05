import numpy;
import random;  
import time;

M = int(input ('Number of lines:')); 
N = int(input ('Number of columns:')); 
K = int(input ('How many evolved states you would like to observe:'));


# create spaces for initial and evolved matrixes 

InSt=[0] * (M+2);
for i in range (M+2):
	InSt[i] = [0] * (N+2);
	
StPlot=[0] * (M);
for i in range (M):
	StPlot[i] = [0] * (N);
	
# function to evaluate how many alive cells are around

def SR(a,b):
	sum = 0;
	for k in range(a-1, a+2):
		for l in range(b-1, b+2):
			#print('InSt[2][3]', InSt[2][3]); 
			sum = sum + InSt[k][l];
	return sum - InSt[a][b];  


#choose type of data you use in the initial state

print('Press R if you want to fill the board with random numbers, press F - if you want to upload numbers from the file'); 
InputDataType = input(); 

#case of random numbers 

if (InputDataType == 'R'): 
	for i in range (1,M+1):
		for j in range (1,N+1):
			InSt[i][j] = random.randint(0, 1);
	print('State # 0');
	for p in range (1, M+1):
		for q in range(1,N+1):
			StPlot[p-1][q-1] = InSt[p][q]; 
		print(StPlot[p-1]);
	print(' ');
    
# case of numbers uploaded from teh .txt file
else: 
	if (InputDataType == 'F'): 
		print('Please, prepare .txt file with your initial state. Note that all numbers must be separated by single spaces and dimensions must correspond to numbers of lines and columns announced above.');
		root = input('Type the path to your .txt file here: ');
		
		matrix = [];
		with open(root) as f: 
			for line in f:
				matrix.append([int(x) for x in line.split()]);
		for i in range (1,M+1):
			for j in range (1,N+1):
				InSt[i][j] = matrix[i-1][j-1];
		print('State # 0');		
		for p in range (1, M+1):
			for q in range(1,N+1):
				StPlot[p-1][q-1] = InSt[p][q]; 
			print(StPlot[p-1]);
		print(' ');
        
# in case type of data is wrong
	else: 
		print('Please, check source of data you want to use and restart the script')
		K = 0; 
		quit();

# how many states we would like to observe 
for k in range(K):
	St=[0] * (M+2);
	for i in range (M+2):
		St[i] = [0] * (N+2); 

	#State evolution rules
	for i in range (1,M+1):
		for j in range (1,N+1):
			if (InSt[i][j] == 1):
				if (SR(i,j) < 2) or (SR(i,j) > 3):
					St[i][j] = 0; 
				else: St[i][j] = 1;
			else:
				if (SR(i,j) == 3):
					St[i][j] = 1;
				else: St[i][j] = 0; 
	time.sleep(1);
# printing the evolved state, reassignment of "new initial state" as current "new state"
	print('State # ', k+1);
	for p in range (1, M+1):
		for q in range(1,N+1):
			StPlot[p-1][q-1] = St[p][q]; 
		print(StPlot[p-1]);
	print(' '); 
	InSt = St;