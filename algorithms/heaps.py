

class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        while i / 2 > 0:
            # if new item is less than parent
            if self.heap_list[i] < self.heap_list[i / 2]:
                tmp = self.heap_list[i / 2]
                # put new item in parents place
                self.heap_list[i / 2] = self.heap_list[i]
                self.heap_list[i] = tmp  # put parent in items place
            i = i / 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)  # positions new item properly

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        elif self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[
            self.current_size]  # set top of heap to last node
        self.current_size = self.current_size - 1
        self.heap_list.pop()  # remove last item
        self.percolate_down(1)
        return retval  # return min and deletes from heap

    def build_heap(self, array):
        i = len(array) / 2
        self.current_size = len(array)
        self.heap_list = [0] + array
        while (i > 0):
            self.percolate_down(i)
            i = i - i
