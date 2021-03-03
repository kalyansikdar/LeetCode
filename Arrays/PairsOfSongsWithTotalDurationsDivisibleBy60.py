import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        tracker = collections.defaultdict(int)
        numberOfPairs = 0

        for t in time:
            remainder = t % 60
            if remainder == 0:
                numberOfPairs += tracker[0]
            else:
                numberOfPairs += tracker[60 - remainder]

            tracker[remainder] += 1

        return numberOfPairs


solution = Solution()
assert solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
assert solution.numPairsDivisibleBy60([60, 60, 60]) == 3
assert solution.numPairsDivisibleBy60([]) == 0
