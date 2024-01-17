class Heap:
    
    def __init__(self, comparer):
        self.heap = []
        self.compare = comparer

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _above_index(self, index1, index2):
        return index2 if self.compare(self.heap[index1], self.heap[index2]) else index1

    def _exchange_positions(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index):
        parent_index = self._parent_index(index)
        while index > 0 and self._above_index(parent_index, index) == index:
            self._exchange_positions(index, parent_index)
            index = parent_index
            parent_index = self._parent_index(index)

    def _heapify_down(self, index):
        size = self.size()
        above_element_index = index

        while True:
            left_child_index = self._left_child_index(index)
            right_child_index = self._right_child_index(index)

            if left_child_index < size and self._above_index(above_element_index, left_child_index) == left_child_index:
                above_element_index = left_child_index

            if right_child_index < size and self._above_index(above_element_index, right_child_index) == right_child_index:
                above_element_index = right_child_index

            if above_element_index != index:
                self._exchange_positions(index, above_element_index)
                index = above_element_index
            else:
                break

    def _readjust(self):
        for i in range((self.size() // 2) - 1, -1, -1):
            self._heapify_down(i)

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(self.size() - 1)

    def pop(self):
        if self.is_empty():
            return None

        pop_element = self.heap[0]
        last_element = self.heap.pop()
        
        if not self.is_empty():
            self.heap[0] = last_element
            self._heapify_down(0)

        return pop_element

    def peek(self):
        return None if self.is_empty() else self.heap[0]

    def find_value(self, value):
        for index, nodo in enumerate(self.heap):
            if value == nodo.valor:
                return index
        return -1

    def delete_node(self, value):
        index = self.find_value(value)
        if index < 0:
            print('Valor no encontrado')

        self._exchange_positions(index, -1)
        self.heap.pop()

        self._readjust()

    def __str__(self):
        return str(list(self.heap))
    
    def print(self):
        for elem in self.heap:
            print(elem.valor, end="\n\n")


class MaxHeap(Heap):
    def __init__(self):
        super().__init__(lambda parent, child: parent.valor < child.valor)

class MinHeap(Heap):
    def __init__(self):
        super().__init__(lambda parent, child: parent.valor > child.valor)
