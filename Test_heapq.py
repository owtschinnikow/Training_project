import time, heapq, random

my_list1, my_list2 = [], []

for i in range(10**6):
    r = random.randint(0, 10**6)
    my_list1.append(r)
    heapq.heappush(my_list2, r)

print(my_list1[0:10], my_list2[0:10], sep = '\n')


t1 = time.time()
my_list1.sort()
print(my_list1[0:10])
t2 = time.time()
print(t2 - t1)

t3 = time.time()
print(heapq.nsmallest(10, my_list2))
t4 = time.time()
print(t4 - t3)

