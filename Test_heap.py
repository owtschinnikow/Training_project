"""

Sample Input:

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:

200
500

Insert {\tt x}x, где 0 \le x \le 10^90≤x≤10 
9
  — целое число;
ExtractMax.

"""

import heapq


heap = []
#print(heap)


def ext(heap):
    """Extract nubber from the heap"""
    n = heapq.heappop(heap)
    return(-n)
    #print(heap)



def add(heap, item):
    """Add nubber in the heap"""
    heapq.heappush(heap, -item)
    #print(heap)


def main():
    n_ = int(input())
    for i in range(n_):
        item = input()
        if item == 'ExtractMax':
            print(ext(heap))
        elif item != 'ExtractMax':
            item = item.split()
            item = item[1]
            item = int(item)
            add(heap, item)  


if __name__ == "__main__":
    main()


