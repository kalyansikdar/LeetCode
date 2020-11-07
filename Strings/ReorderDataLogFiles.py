class Solution:
    def reorderLogFiles(self, logs):
        letterLogs, digitLogs = [], []
        for log in logs:
            words = log.split(" ")
            if words[1][0].isalpha():
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        letterLogs.sort(key=lambda x: x.split()[0])
        letterLogs.sort(key=lambda x: x.split()[1:])
        letterLogs.extend(digitLogs)

        return letterLogs


solution = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
expectedResult = ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print (solution.reorderLogFiles(logs))
assert expectedResult == solution.reorderLogFiles(logs)