class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach with left and right windows
        # Left and right starts from 0
        left, right = 0, 0
        # maintain a set to hold unique chars
        seenChars = set()
        longestStr = 0

        # right index is iterating
        while right < len(s):
            # till right char is available in seenChar, remove left chars
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1

            # add to set
            seenChars.add(s[right])
            # maintain longest str
            longestStr = max(longestStr, right - left + 1)

            right += 1

        return longestStr


solution = Solution()
s = "pwwkew"
assert solution.lengthOfLongestSubstring(s) == 3
s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3