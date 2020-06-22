class Solution:
    """
    This solution exceeds time limit
    """
    def trap_exceeded(self, height):
        totalTillEnd = 0

        for i in range(1, len(height)):
            left, right = height[i], height[i]
            currIndex = i

            while i >= 0:
                left = max(left, height[i])
                i -= 1

            i = currIndex       # above while loop takes i to left most index
            while i < len(height):
                right = max(right, height[i])
                i += 1

            diff = min(left, right)
            totalTemp = diff - height[currIndex]
            # print(currIndex, height[currIndex], left, right, diff, totalTemp, totalTillEnd)
            totalTillEnd += totalTemp

        return totalTillEnd

    def trap_passed(self, height) -> int:
        totalTillEnd = 0
        left = [0]
        right = [0] * (len(height))     # had to pre-populate the list as it's complex to append to the left, instead
        # updating the value

        # create a list to show max height on it's left at every index
        for i in range(1, len(height)):
            left.append(max(left[i - 1], height[i - 1]))

        # create a list to show max height on it's right at every index
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        for i in range(len(height)):
            waterAtIndex = min(left[i], right[i]) - height[i]
            if waterAtIndex > 0:
                totalTillEnd += waterAtIndex

        return totalTillEnd


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = solution.trap_passed(height)
print (result)
