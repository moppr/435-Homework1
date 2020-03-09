class MaxHeap:
    '''A simple max heap using an array as storage'''
    
    def __init__(self):
        self.heap = []
        
    def left(self, i):
        return 2*i + 1
    
    def get_left(self, i):
        try:
            left = self.heap[self.left(i)]
        except:
            left = -1
        return left
    
    def right(self, i):
        return 2*i + 2
    
    def get_right(self, i):
        try:
            right = self.heap[self.right(i)]
        except:
            right = -1
        return right
    
    def parent(self, i):
        return -10 if i == 0 else (i-1)//2
        
    def max_lookup(self):
        '''Return the maximum value in the heap.'''
        return self.heap[0]
        
    def extract_max(self):
        '''Remove the max element from the heap.'''
        self.delete(0)
    
    def delete(self, i):
        '''Remove element at the given index while maintaining heap order.'''
        self.swap(i, len(self.heap)-1)
        self.heap.pop(len(self.heap)-1)
        self.heapify_down(0)
        
    def heapify_down(self, i):
        '''Check children from given index and fix if out of order.'''
        #check if there is any child with a value greater than current
        left = self.get_left(i)
        right = self.get_right(i)
        
        # while there is a child node with greater value than current, swap and set current to child
        while left > self.heap[i] or right > self.heap[i]:
            child = self.index_of_greatest_child(i)
            self.swap(i, child)
            i = child
            left = self.get_left(i)
            right = self.get_right(i)
            
    def index_of_greatest_child(self, i):
        '''Return index of child with the greater value.'''
        left = self.get_left(i)
        right = self.get_right(i)
        
        return self.right(i) if right > left else self.left(i)
        
    def insert(self, value):
        '''Add a given value to the heap.'''
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)
        
    def heapifyUp(self, i):
        '''Move element at the given index to the right position.'''
        while self.parent(i) != -10 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
            
    def swap(self, i, j):
        '''Swap two elements at the given indices.'''
        first_element = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = first_element
        

if __name__ == '__main__':

    # parsing inputs
    num_commands = int(input())
    commands = [input() for _ in range(num_commands)]
    
    heap = MaxHeap()
    
    for command in commands:
        if command == 'size':
            print(len(heap.heap))
        elif 'insert' in command:
            heap.insert(int(command.split()[-1]))
        elif command == 'maxLookup':
            print(heap.max_lookup())
        elif command == 'extractMax':
            heap.extract_max()
        else: # delete
            heap.delete(int(command.split()[-1]))
