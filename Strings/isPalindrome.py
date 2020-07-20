class Solution:
    def isPalindrome(self, s: str) -> bool:
        holder = []
        for ch in s:
            if ch.isalnum():
                holder.append(ch.lower())

        start, end = 0, len(holder) - 1

        while start < end:
            if holder[start] != holder[end]:
                return False
            start += 1
            end -= 1

        return True

    def isPalindrome_better(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1

        return True


solution = Solution()
s= "A man, a plan, a canal: Panama"
s1 = "race a car"
print (solution.isPalindrome_better(s))