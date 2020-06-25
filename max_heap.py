from copy import deepcopy
def insert(ele,heap):
        if len(heap) == 0: 
            heap.append(ele)
            return 
        max_heapify(ele, heap)

def parentfind(index):
        return index//2

def bubbleUp(parent, child, heap):
        if heap[child][1] > heap[parent][1]:
            temp = deepcopy(heap[parent])
            heap[parent] = deepcopy(heap[child])
            heap[child] = deepcopy(temp)
            bubbleUp(parentfind(parent), parent, heap)

def max_heapify(ele,heap):
        heap.append(ele)
        index = len(heap) - 1
        bubbleUp(parentfind(index), index, heap)

def pop(heap):
    return heap.pop(0)

if __name__ == "__main__":
    test()