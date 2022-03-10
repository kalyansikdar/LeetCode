class Solution:
    def largestRectangleArea(self, heights) -> int:
        left, right = [0] * len(heights), [0] * len(heights)
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            if not stack:
                left[i] = 0
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    popped = stack.pop()

                if not stack:
                    left[i] = 0
                else:
                    left[i] = stack[-1] + 1
                stack.append(i)

        while stack:
            stack.pop()

        for i in range(len(heights) - 1, -1, -1):
            if not stack:
                right[i] = len(heights) - 1
                stack.append(i)

            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    popped = stack.pop()

                if not stack:
                    right[i] = len(heights) - 1
                else:
                    right[i] = stack[-1] - 1
                stack.append(i)

        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] + 1))

        return maxArea


solution = Solution()
assert solution.largestRectangleArea([2,1,5,6,2,3]) == 10
assert solution.largestRectangleArea([2,4]) == 4