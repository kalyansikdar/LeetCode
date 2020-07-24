import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = collections.Counter(s)

        for ch in t:
            if ch in freq:
                freq[ch] -= 1
            else:
                return False

        for k, v in freq.items():
            if v > 0:
                return False

        return True


solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))
