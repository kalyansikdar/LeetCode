class Solution:
    def findDuplicate_CycleDetection(self, nums) -> int:
        """
        This solution is similar to Linked List loop detection problem, please refer to CTCI for details
        """
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:  # means the overlapping position is found, and after k steps the loop has started. also
                # after k steps of the starting position loop started
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

    def findDuplicate(self, nums) -> int:
        """
        This solution uses extra space, as per the question, it's not valid
        """
        holder = {}
        for i in nums:
            if i not in holder:
                holder[i] = 1
            else:
                holder[i] += 1

        for k, v in holder.items():
            if holder[k] > 1:
                return k


solution = Solution()
nums = [3, 1, 3, 4, 2]
result = solution.findDuplicate_CycleDetection(nums)
print(result)
# IMPORTANT: Cycle detection can be applied here because the conditions are there n+1 numbers in the given list and
# the numbers have to be taken from 1->n. So, in the above list, the numbers can be from only 1 to 4, where as the
# total size of the list is 5
