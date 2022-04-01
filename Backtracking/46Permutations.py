class Solution:

    def permute(self, nums):
        # Example: [1, 2, 3]
        result = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            # take one num off
            n = nums.pop(0)
            # [2, 3]
            # find permutations of the rest of the nums
            perms = self.permute(nums)

            for p in perms:
                # add the taken off num to the permutation of rest of nums
                p.append(n) # [2, 3, 1]/[3, 2, 1]
                result.append(p)

            # backtrack: put the element back to nums, for previous branches after backtrack
            nums.append(n)

        return result


solution = Solution()
nums = [1, 2, 3]
assert solution.permute(nums) == [[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[1,2,3]]