import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        paragraph = paragraph.lower()
        bannedWords = set(banned)

        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, ' ')

        freq = {}
        maxVal, result = 0, ""
        words = paragraph.split(" ")
        print(words)

        for word in words:
            if word in bannedWords or word == '':
                continue
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

            if freq[word] > maxVal:
                result, maxVal = word, freq[word]

        return result

solution = Solution()
paragraph =  "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print (solution.mostCommonWord(paragraph, banned))