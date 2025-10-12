# spador

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize min-heap to store k largest elements
        # Min-heap property: parent <= children, root is smallest element
        self.minHeap = nums
        self.k = k
        
        # Convert list to heap in O(n) time
        heapq.heapify(self.minHeap)
        
        # Keep only k largest elements in the heap
        # Remove smallest elements until heap size = k
        # This ensures we maintain only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove smallest element
        

    def add(self, val: int) -> int:
        # Add new element to the heap
        heapq.heappush(self.minHeap, val)
        
        # If heap size exceeds k, remove the smallest element
        # This maintains the property that we only keep k largest elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Return the root of min-heap (smallest among k largest = kth largest overall)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
