class Item(object):
    """
    from Introduction to Computation and Programming Using Python
    """
    def __init__(self, name, value, weight):
        self.name = name
        self.value = float(value)
        self.weight = float(weight)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeoght(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result


def knapsack(items, capacity):
    import numpy as np

    A = np.zeros(items, capacity)

    for i in range(capacity):
        for x in range(items):
            A[i, x] = max(A[i - 1, x], A[i - 1, x - items.w[i]] + items.w[x])

    return A[x, w]


