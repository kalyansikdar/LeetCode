class Solution:
    def twoSum(self, nums, target: int):
        """
        One pass solution, TC: O(N)
        """
        diffTracker = {}
        # insert the diff into a map with value as index
        # look for the diff in tracker, if found, viola!!
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in diffTracker:
                return [diffTracker[diff], i]

            diffTracker[nums[i]] = i

    def twoSum(self, nums, target: int):
        """
        Regular solution - TC: O(N^2)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
assert solution.twoSum(nums, target) == [0, 1]