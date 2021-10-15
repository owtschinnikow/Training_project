# put your python code here

"""
Sample Input: 5
2 3 9 2 9
Sample Output: 2
"""

def merge(a, b):
    #print('a', a, 'b', b)
    tmp = []
    #print('tmp_start', tmp)
    global k
    #print('k', k)
    while a and b:
        if a[0] <= b[0]:
            tmp.append(a.pop(0))
            #print('tmp_if', tmp)
        else:
            tmp.append(b.pop(0))
            #print('tmp_else', tmp)
            k += len(a)
    tmp.extend(a or b)
    #print('tmp_end', tmp)
    return tmp


def mergesort(lst):
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    return merge(mergesort(lst[: m]), mergesort(lst[m:]))
    

def main():
    n = 5 #int(input())
    #print('n', n)
    queue = [2, 3, 9, 2, 9] #[int(i) for i in input().split()]
    #print('queue', queue)
    mergesort(queue)
    print(k) #('k_end', k)


if __name__ == '__main__':
    k = 0
    main()
