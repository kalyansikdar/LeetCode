import datetime
class LRUCache:
    """
    Time exceeded for this solution
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.count = 0      # keeps count of the total number of keys
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache[key][1] = datetime.datetime.now().time()     # updates the existing value with new key and
            # updates current timestamp
            return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:       # if key is not there, it's added, else it's time is updated
            self.count += 1
        self.cache[key] = [value, datetime.datetime.now().time()]

        if self.count > self.capacity:      # whenever count exceeds the capacity, it sorts the cache values by
            # second element which is it's time when it was added to the cache, and deletes the element with oldest
            # timestamp and decreases the count by 1
            lru_item = sorted(self.cache.items(), key=lambda x: x[1][1])[0]
            del self.cache[lru_item[0]]
            self.count -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)