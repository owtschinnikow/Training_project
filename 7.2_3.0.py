import sys
from bisect import bisect_left

def find_pos(xs, query):
    lo = bisect_left(xs, query)
    # i < lo : xs[i] < query
    # i > lo : xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1       # 1-based
    else:
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
    main()