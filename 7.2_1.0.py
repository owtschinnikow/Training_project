import sys


def find_pos(xs, query):
    try:
        return xs.index(query) + 1
    except ValueError:
        return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin) # Get-Content 7.2_1.0.txt | python 7.2_1.0.py
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == "__main__":
    main()