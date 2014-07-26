def knapsack(items, capacity):

    import numpy as np

    A = np.zeros(items, capacity)

    for i in range(capacity):
        for x in range(items):
            A[i, x] = max(A[i-1, x],A[i-1, x-items.w[i]] + items.w[x])

    return A[x, w]


