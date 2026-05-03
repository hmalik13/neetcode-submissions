class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # keys map to node which contains key-value pair
        self.cache = {} 
        # create dummy nodes: left = LRU, right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        # point the dummy nodes at each other
        self.left.next = self.right
        self.right.prev = self.left

    # helper function to remove LRU node
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # helper function to insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the node then reinsert it since
            # this is now the most recently used key
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # remove node if already in cache
        # then insert new node 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # remove LRU key if capacity is exceeded
        if len(self.cache) > self.capacity:
            # since we're always inserting most recently used
            # node to the right, the LRU key is the leftmost node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

