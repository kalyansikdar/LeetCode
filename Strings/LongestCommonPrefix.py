class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        This Solution is O(n2). Basically Nlogn for sorting and then N2 again, overall O(N2)
        :param strs:
        :return:
        """
        if not strs:
            return ""

        strs.sort()

        firstWord = strs[0]
        wordLen = len(firstWord)
        prefix = ""

        for i in range(wordLen):
            letter = firstWord[i]
            for j in range(1, len(strs)):
                if strs[j][i] != letter:
                    return prefix

            prefix += letter
        return prefix

    def longestCommonPrefix2(self, strs) -> str:
        """
        This is also O(N2). But N+0(N2) ~ O(N2)
        :param strs:
        :return:
        """
        if not strs:
            return ""

        minWordLen = len(strs[0])
        for s in strs:
            minWordLen = min(minWordLen, len(s))

        prefix = ""

        for i in range(minWordLen):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != letter:
                    return prefix

            prefix += letter
        return prefix


solution = Solution()
nums = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix2(nums)
print("Longest Common Prefix: ", result)
