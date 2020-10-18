#matrix creation of n * n 
import itertools 
  
# initializing N 
N = 4
  
# printing dimension 
print("The dimension : " + str(N)) 
  
# using next() + itertools.count() 
# matrix creation of n * n 
temp = itertools.count(1)  
res = [[next(temp) for i in range(N)] for i in range(N)] 
  
# print result 
print("The created matrix of N * N: " + str(res)) 