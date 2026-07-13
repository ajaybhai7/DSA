import time

start_time = time.time()

list1 = [i for i in range(1,1000000, 2)]

print(list1[1000])
print(time.time() - start_time)