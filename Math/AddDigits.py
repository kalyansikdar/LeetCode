class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            n = 0
            while num > 0:
                n += num % 10
                num = num // 10

            num = n

        return num


solution = Solution()
num = 3856
print (solution.addDigits(num))