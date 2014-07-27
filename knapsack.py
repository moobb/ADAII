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

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result


def buildItems():
    names = ['a', 'b', 'c', 'd']
    values = [3, 2, 4, 4]
    weights = [4, 3, 2, 3]
    Items = []
    for i in range(0, len(values)):
        Items.append(Item(names[i], values[i], weights[i]))

    # dummy item
    Items.insert(0, ('', 0, 0))
    return Items


def knapsack(items, capacity):
    import numpy as np

    numberItems = len(items)
    A = np.zeros((numberItems+1, capacity+1))

    for i in range(1, numberItems):
        for x in range(capacity+1):
            if x - items[i].getWeight() >= 0:
                secondTerm = A[i - 1, x - items[i].getWeight()] + items[i].getValue()
            else:
                secondTerm = 0
            A[i, x] = max(A[i - 1, x], secondTerm)

    return A[i, x]

#items = buildItems()
#a = knapsack(items, 6)


