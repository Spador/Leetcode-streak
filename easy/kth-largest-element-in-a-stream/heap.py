# Basic Min-Heap Implementation
# Contains the essential functions needed for heap operations

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Get parent index of node at index i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index of node at index i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index of node at index i"""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        """Maintain heap property by moving element up"""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        """Maintain heap property by moving element down"""
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Find smallest among node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        # If smallest is not the current node, swap and continue
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)
    
    def insert(self, val):
        """Insert a new element into the heap"""
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """Remove and return the minimum element"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def peek(self):
        """Return the minimum element without removing it"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return the number of elements in the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def heapify(self, arr):
        """Convert an array into a min-heap in O(n) time"""
        self.heap = arr[:]
        # Start from the last non-leaf node and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)


# Example usage:
# heap = MinHeap()
# heap.heapify([4, 5, 8, 2])  # Convert array to heap
# heap.insert(3)              # Insert new element
# min_val = heap.extract_min() # Remove minimum
# print(heap.peek())          # Get minimum without removing
