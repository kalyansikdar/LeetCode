class Solution:
    def compress(self, chars) -> int:
        if len(chars) <= 1:
            return chars

        prev = chars[0]
        uniqueChar = 0
        eachCharCount = 0

        for idx, ch in enumerate(chars):
            if ch != prev:
                uniqueChar += 1
                chars[(uniqueChar * 2) - 1] = str(eachCharCount)
                eachCharCount = 0

            eachCharCount += 1
            prev = ch

        if eachCharCount > 0:
            uniqueChar += 1

        chars[(uniqueChar) * 2 - 1] = str(eachCharCount)

        return chars[:(uniqueChar) * 2]


solution = Solution()
chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(solution.compress(chars))