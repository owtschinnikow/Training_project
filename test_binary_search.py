

def left_bound(A, key):
    """
    Поиск левой границы в массиве
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    """
    Поиск правой границы в массиве
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


A = [1, 3, 3, 5, 6, 7, 8]
key = 6
print('pos = ' + str(left_bound(A, key)),
      A[left_bound(A, key)],
      'pos = ' + str(right_bound(A, key)),
      A[right_bound(A, key)], sep='\n')
