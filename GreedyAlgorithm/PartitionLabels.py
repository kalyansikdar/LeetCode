from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {}
        # create a dict to indicate the last index of each char in the input
        for idx, ch in enumerate(S):
            lastIndex[ch] = idx

        print(lastIndex)

        start = 0
        end = None
        result = []

        for idx, ch in enumerate(S):
            # even ever end is None, we will have to assign the last index of first char to it.
            if end == None:
                end = lastIndex[S[start]]
            # if within the initial substring, if any char's last index is beyond end index, we will have to expand
            # the substring till end of that char
            if lastIndex[ch] > end:
                end = lastIndex[ch]
            # if index has reached end, then it's the end of a substring, add it to the result, set start at the
            # first char of next substring and end to None
            if idx == end:
                result.append(end - start + 1)
                start = end + 1
                end = None

        return result


solution = Solution()
S = "ababcbacadefegdehijhklij"
assert solution.partitionLabels(S) == [9,7,8]
S = "qiejxqfnqceocmy"
assert solution.partitionLabels(S) == [13, 1, 1]
