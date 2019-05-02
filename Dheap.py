class D_aryHeap:
    def __init__(self, d):
        self.items = []
        self.d = d

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1) // self.d

    def child(self, index, position):
        return index * self.d + (position + 1)

    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, i):
        largest = i
        for j in range(self.d):
            c = self.child(i, j)
            if (c < self.size() and self.get(c) > self.get(largest)):
                largest = c
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, key):
        index = self.size()
        self.items.append(key)
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p


if __name__ == '__main__':
    object= D_aryHeap(4)
    array=[6,23,12,15,6]
    for x in array:
        object.insert(x)
    print(object.get_max())
    print(object.extract_max())
    print(object.get_max())


