import time

def print_lines(i):
    print("line: ",i)
    
input = ['A','B','C','D']

for i in input:
    start = time.time()
    print_lines(i)
    end = time.time()
    print("Time taken for ",i," : %s",str(end - start))