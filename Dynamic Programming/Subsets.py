class Solution:
    def subsets_iterative(self, nums):
        result = []
        result.append([])

        for item in nums:
            result += [i + [item] for i in result]
# order of result being filled: [] -> [],[1] -> [], [2], [1], [1,2] -> [], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]
        return result

    def subsets_recursive(self, nums):
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, index, current, result):
        result.append(current)

        for i in range(index, len(nums)):
            self.dfs(nums, i+1, current + [nums[i]], result)


solution = Solution()
nums= [1,2,3]
print (solution.subsets_iterative(nums))
print (solution.subsets_recursive(nums))