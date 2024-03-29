class MyHashMap:
    """
    This is a naive implementation where the size of the map is considered as 10000001. As per question, keys will
    be in range of [0, 1000000], there is no possibility of collision.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._v = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self._v[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self._v[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self._v[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)