class Solution:
    def reverseList(self, words, start, end):
        # reverse each element in a list
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        # O(n) solution
        words = s.strip().split()
        start, end = 0, (len(words) - 1)

        self.reverseList(words, start, end)
        return " ".join(words)


solution = Solution()
sentence1 = "the sky is blue"
sentence2 = "  hello world!  "
sentence3 = "a good   example"
print(solution.reverseWords(sentence1))
print(solution.reverseWords(sentence2))
print(solution.reverseWords(sentence3))