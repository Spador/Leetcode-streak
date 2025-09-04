##spador

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}               # This dictionary will map keys to node
        
        # left = LRU and right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # Deletes node from anywhere
    def delete(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node from right because MRU
    def insert(self, node: Node):
        node.next, node.prev = self.right, self.right.prev
        node.prev.next = node.next.prev = node

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If the capacity of Cache is full then remove the LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)            # remove it from linked list
            del self.cache[lru.key]     # remove it from cache


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
