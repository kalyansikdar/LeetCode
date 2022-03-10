class Solution:
    def dailyTemperatures(self, T):
        """
        Algorithm: Monotonic stack: Form a decreasing stack
        for every element -
            - if stack is empty, insert index, value into stack
            - if not, if current temp is greater than stack top element value, pop from stack one by one
            - for every case, (index - popped index) would be the number of days to wait till a warmer temp
        """
        result = [0] * len(T)
        stack = []

        for idx, t in enumerate(T):
            while stack and t > stack[-1][1]:
                prev_i, prev_val = stack.pop()
                result[prev_i] = idx - prev_i

            stack.append((idx, t))

        return result


solution = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution.dailyTemperatures(T))