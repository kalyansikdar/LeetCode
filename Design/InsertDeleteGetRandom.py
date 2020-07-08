import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        self.map = {}       # this dict to keep track of the indices of the elements

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        else:
            self.numbers.append(val)
            self.map[val] = len(self.numbers) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        else:
            idxToDelete = self.map[val]
            lastVal = self.numbers[len(self.numbers) - 1]
            self.numbers[idxToDelete] = lastVal     # element to be deleted is being overwritten by the last element
            self.map[lastVal] = idxToDelete

            self.numbers.pop()      # deleting the last element as it has been stored in the deleted element's place
            del self.map[val]       # delete element is being deleted from map as well

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randomVal = random.randint(0, len(self.numbers) - 1)
        return self.numbers[randomVal]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


solution = RandomizedSet()
print(solution.insert(1))
print(solution.insert(5))
print(solution.insert(7))
print(solution.insert(9))
print(solution.getRandom())
print(solution.remove(5))
print(solution.remove(4))
print(solution.insert(4))
print(solution.getRandom())
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()