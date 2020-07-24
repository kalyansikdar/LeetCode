class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seenStr = set()
        maxVal = 0

        while j < len(s):
            if s[j] not in seenStr:
                seenStr.add(s[j])
                j += 1
                maxVal = max(maxVal, len(seenStr))
            else:
            # if the ith ch is removed, the seenStr may not have the non-repeating characters but maxVal will be correct
                seenStr.remove(s[i])
                i += 1

        return maxVal


solution = Solution()
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))