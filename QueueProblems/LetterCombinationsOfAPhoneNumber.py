import collections
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        queue = collections.deque()
        result = []

        # if input is empty, return empty queue
        if len(digits) == 0:
            return queue

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(
        # n) time complexity

        queue.append("")

        for digit in digits:
            lettersMapped = mapping[digit]  # abc
            s = len(queue)

            while s:
                element = queue.popleft()
                for ch in lettersMapped:
                    queue.append(element + ch)

                s -= 1

        while queue:
            result.append(queue.popleft())

        return result


# Time complexity:
# N = 0 -> output length = 0 = 3^0
# N = 1 -> output length = 3 = 3^1
# N = 2 -> output length = 9 = 3^2
# N = 3 -> output length = 27 = 3^3 = K^N where K is length of letter assigned to each digit

solution = Solution()
assert solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert solution.letterCombinations("75") == ["pj","pk","pl","qj","qk","ql","rj","rk","rl","sj","sk","sl"]