from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time complexity O(N) because it's one pass
        carry = 0
        # iterate from end and add one to last digit. If last digit is 9, need to carry 1 to the next digit
        for i in range(len(digits) - 1, -1, -1):
            # If this is the last digit, need to add 1 as per the requirement
            if i == len(digits) - 1:
                if digits[i] + 1 > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
            else:
                # If this is NOT the last digit, need to add carry, if any
                if digits[i] + carry > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] = digits[i] + carry
                    carry = 0

        if carry == 1:
            digits.insert(0, 1)

        return digits

    def plusOne_better(self, digits):
        carry = 1
        n = len(digits) - 1

        while carry and n >= 0:
            if digits[n] < 9:
                carry = 0
                digits[n] += 1
            else:
                digits[n] = 0
            n -= 1

        if carry == 1:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


solution = Solution()
digits = [1,2,3]
assert solution.plusOne(digits) == [1,2,4]
digits = [4,3,2,1]
assert solution.plusOne(digits) == [4,3,2,2]
digits = [0]
assert solution.plusOne(digits) == [1]
digits = [4,5,9,9]
assert solution.plusOne(digits) == [4,6,0,0]
digits = [9]
assert solution.plusOne(digits) == [1,0]