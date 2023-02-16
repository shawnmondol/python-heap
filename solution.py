"""
Ian Barber,Alex Woodring, Max Huang, and Angelo Savich
Project 8 - Heaps - Solution Code
CSE 331 Spring 2022

"""
import math
from typing import List, Tuple, Any


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
            Gets the length of the MinHeap
            :return: Length of the data set
        """
        return len(self.data)

    def empty(self) -> bool:
        """
            Sees if the MinHeap data set is empty
            :return: True if empty
        """
        return len(self.data) == 0

    def top(self) -> int:
        """
            Gets the top of the MinHeap
            :return: First index of our data set
        """
        if self.empty():
            return None
        return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
            Gets the index of the left child
            :param index: index to find the child of
            :return: left child of the index
        """
        child = 2 * index + 1
        x = len(self.data)
        if child >= len(self.data):
            return None
        return child

    def get_right_child_index(self, index: int) -> int:
        """
            Gets the index of the right child
            :param index: index to find the child of
            :return: right child of the index
        """
        child = 2 * index + 2
        x = len(self.data)
        if child >= len(self.data):
            return None
        return child

    def get_parent_index(self, index) -> int:
        """
            Gets the parent index of the child
            :param index: child index
            :return: parent index of the child
        """
        if index == 0:
            return None
        return math.floor((index - 1)/2)

    def get_min_child_index(self, index: int) -> int:
        """
            Gets the index of the child with the lowest value
            :param index: Parent index
            :return: child with the lowest value
        """
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)
        if left_child is not None and right_child is not None:
            if(self.data[left_child] < self.data[right_child]):
                return left_child
        if left_child is None:
            return right_child
        if right_child is None:
            return left_child
        return right_child

    def percolate_up(self, index: int) -> None:
        """
            Percolates up the value at index to its valid spot in the heap
            :param index: index to percolate
            :return: None
        """
        while (index > 0):
            parentIndex = self.get_parent_index(index)
            if self.data[index] >= self.data[parentIndex]:
                return
            else:
                self.data[index], self.data[parentIndex] = self.data[parentIndex], self.data[index]
                index = parentIndex

    def percolate_down(self, index: int) -> None:
        """
            Percolates down the value at index to its valid spot in the heap
            :param index: index to percolate
            :return: None
        """
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)
        if left_child is not None and right_child is not None:
            if self.data[index] > self.data[left_child] or self.data[index] > self.data[right_child]:
                if self.data[left_child] < self.data[right_child]:
                    self.data[index], self.data[left_child] = self.data[left_child], self.data[index]
                    self.percolate_down(left_child)
                else:
                    self.data[index], self.data[right_child] = self.data[right_child], self.data[index]
                    self.percolate_down(right_child)
        elif left_child is not None:
            if self.data[index] > self.data[left_child]:
                self.data[index], self.data[left_child] = self.data[left_child], self.data[index]
        elif right_child is not None:
            if self.data[index] > self.data[right_child]:
                self.data[index], self.data[right_child] = self.data[right_child], self.data[index]

    def push(self, val: int) -> None:
        """
            Appends value to the end of our data set
            then percolates it up to a valid position
            :param val: value to add
            :return: None
        """
        self.data.append(val)
        self.percolate_up(len(self.data) - 1)

    def pop(self) -> int:
        """
            Removes the top of our data set
            then percolates it down to a valid position
            :return: value that was removed
        """
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        pop = self.data.pop()
        self.percolate_down(0)
        return pop

class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
            DOC STRING GOES HERE
        """
        return len(self.data) == 0

    def top(self) -> int:
        """
            DOC STRING GOES HERE
        """
        if self.empty():
            return None
        return -self.data.top()

    def push(self, key: int) -> None:
        """
            Appends value to the end of our data set
            then percolates it up to a valid position
            :param val: value to add
            :return: None
        """
        self.data.push(-key)

    def pop(self) -> int:
        """
            Removes the top of our data set
            then percolates it down to a valid position
            :return: value that was removed
        """

        return -self.data.pop()

#https://www.youtube.com/watch?v=VmogG01IjYc
def current_medians(values) -> List[int]:
    """
        Uses heaps to find the running median
        :param values: List of values to sequentially find
        the median of
        :return: List of gathered medians
    """

    def adjust_size(minheap, maxheap):
        """
            Evens out sides when the threshold is exceeded by moving
            values from the larger side to the smaller side
            :param minheap: the minheap
            :param maxheap: the maxheap
            :return: None
        """
        larger = minheap if len(minheap) > len(maxheap) else maxheap
        smaller = maxheap if len(minheap) > len(maxheap) else minheap
        if len(larger) - len(smaller) > 1:
            smaller.push(larger.pop())

    def get_median(minheap, maxheap):
        """
            Gets the median from the heaps if sizes are the same,
            or else the top of the larger heap is returned
            :param minheap: the minheap
            :param maxheap: the maxheap
            :return: median of the heaps
        """
        larger = minheap if len(minheap) > len(maxheap) else maxheap
        smaller = maxheap if len(minheap) > len(maxheap) else minheap
        if len(larger) == len(smaller):
            return (larger.top() + smaller.top()) / 2
        else:
            return larger.top()

    maxheap = MaxHeap()
    minheap = MinHeap()
    medians = []

    for value in values:
        if (maxheap.empty() or value < maxheap.top()):
            maxheap.push(value)
        else:
            minheap.push(value)
        adjust_size(minheap, maxheap)
        medians.append(get_median(minheap, maxheap))

    return medians