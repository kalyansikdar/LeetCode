class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # create doubly linked list
        # left denotes least recently used key, right denotes latest key
        # when a key is inserted, it has to be added just before right
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertBeforeRight(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertBeforeRight(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def insertBeforeRight(self, Node):
        prev = self.right.prev
        nxt = self.right
        prev.next = Node
        nxt.prev = Node
        Node.next = nxt
        Node.prev = prev

    def remove(self, Node):
        prev = Node.prev
        nxt = Node.next
        prev.next = nxt
        nxt.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)