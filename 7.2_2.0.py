import sys


def find_pos(xs, query):
    """ Invariant: lo <= pos < hi """
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:
            hi = mid        # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1    # [mid + 1, hi]
        else:
            return mid + 1  # 1 - based
    return -1


def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1
    print("Test - All OK")

def main():
    reader = (map(int, line.split()) for line in sys.stdin) # Get-Content 7.2_1.0.txt | python 7.2_1.0.py
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")


if __name__ == "__main__":
    test() #main()