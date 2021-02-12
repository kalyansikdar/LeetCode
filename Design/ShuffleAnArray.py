from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.originalArr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.originalArr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # IMPORTANT: normally when we do new_list = old_list, it creates a new reference to the old list, so even if changes are
        # made to new_list, the original list is changed.
        dupArray = self.originalArr.copy()  # create a shallow copy of the list
        shuffledArray = []

        for i in range(len(self.originalArr)):
            remove_idx = random.randrange(len(dupArray))
            shuffledArray.append(dupArray.pop(remove_idx))

        return shuffledArray