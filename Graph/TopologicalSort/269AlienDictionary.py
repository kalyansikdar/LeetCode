from typing import (
    List,
)


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # This was run in Lintcode, not in Leetcode
        # However, it did not pass all the test cases
        adjMap = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))

            # invalid case (w1 = "ert", e2 = "er"). er should have been before ert by definition
            # hence, invalid dictionary
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # check till the minLen and add the dependency when there is a difference
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjMap[w1[j]] = w2[j]
                    break

        print('adjMap', adjMap)
        # apply topological sort
        topologicalSort = []
        inDegrees = {c: 0 for w in words for c in w}

        for k, v in adjMap.items():
            for j in v:
                inDegrees[j] += 1
        print('inDegrees:', inDegrees)

        queue = []
        for k, v in inDegrees.items():
            if v == 0:
                queue.append(k)

        print(queue)
        while queue:
            c = queue.pop(0)
            topologicalSort.append(c)

            followers = adjMap[c]

            for f in followers:
                inDegrees[f] -= 1

                if inDegrees[f] == 0:
                    queue.append(f)

        return "".join(topologicalSort)


solution = Solution()
words = ["wrt","wrf","er","ett","rftt"]
assert solution.alien_order(words) == "wertf"