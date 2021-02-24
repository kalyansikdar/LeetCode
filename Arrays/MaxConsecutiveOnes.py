from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # loop over the input, if any element is 1 add to tempCount, else if the tempCount is greater than
        # finalCount, update it and reset the finalCount
        # TC: O(N)
        finalCount = 0
        tempCount = 0

        for i in nums:
            if i == 1:
                tempCount += 1
            else:
                finalCount = max(finalCount, tempCount)
                tempCount = 0

        # if max consecutive ones are at the end
        finalCount = max(finalCount, tempCount)

        return finalCount

    def findMaxConsecutiveOnes_different(self, nums):
        count = 0
        answer = 0
        for num in nums:
            if num == 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 0
        return answer


solution = Solution()
nums = [1, 0, 1, 1, 0, 1]
assert solution.findMaxConsecutiveOnes(nums) == 2
nums = [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
assert solution.findMaxConsecutiveOnes(nums) == 5
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
assert solution.findMaxConsecutiveOnes(nums) == 10
nums = [1, 0, 1, 1, 0, 1]
assert solution.findMaxConsecutiveOnes_different(nums) == 2
nums = [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
assert solution.findMaxConsecutiveOnes_different(nums) == 5
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
assert solution.findMaxConsecutiveOnes_different(nums) == 10
