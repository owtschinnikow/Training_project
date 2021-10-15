"""
прыжки кузнечика
"""
from mpl_toolkits.axes_grid1.axes_size import Fixed


def count_trajectories(N, allowed:list):
    """
    прыжки кузнечика
    шаг - +1 +2 +3
    allowed - список True или False с запрещёнными ячейками
    """
    k = [0, 1, int(allowed) + [0]*(N-3)]
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[N]


"""
Минимальная стоимость достижения клетки N Кузнечиком
"""

def count_min_cost(N, price:list):
    C = [float('-inf'), price[1], price[1] + price[2]] + [0]*(n-2)
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]


