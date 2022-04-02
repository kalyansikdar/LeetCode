class Solution:
    def twoSum(self, numbers, target: int):
        # Two pointers approach, utilizing 'sorted' property of the array
        start, end = 0, len(numbers) - 1

        while start <= end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            # as input array is sorted, if the sum is larger than the target, i.e.
            # we need to sum smaller number, move end to left, end points to larger number
            elif numbers[start] + numbers[end] > target:
                end -= 1
            # start points to smaller number,
            # if sum is smaller, move start towards larger number to right
            else:
                start += 1