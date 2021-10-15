"""
Практика на Python: Непрерывный рюкзак
"""

import heapq
import sys

def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    
    acc = 0
    while order:
        v_per_w, w = heapq.heappop(order)
        if w < capacity:
            acc += -v_per_w * w
            capacity -= w
        else:
            acc += -v_per_w * capacity
            break
        
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin) # Генератор для стандатрого ввода, разбивает сроку на куски и приводит каждый кусок к целому куску
    n, capacity = next(reader) # чтение входа опросом следующего элемента из генератора
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))   


if __name__ == "__main__":
    main()


