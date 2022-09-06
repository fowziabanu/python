import time
import concurrent.futures

def print_lines(i):
    print("line: ",i)
    
input = ['A','B','C','D']

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in input:
        start = time.time()
        futures.append(executor.submit(print_lines, i))
        end = time.time()
        for future in concurrent.futures.as_completed(futures):
            print("Time taken for ",i," : %s",str(end - start))