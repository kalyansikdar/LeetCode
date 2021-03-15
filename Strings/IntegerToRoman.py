class Solution:
    def intToRoman(self, num: int) -> str:
        """
        TC is 0(1) because we are looping thru intToRomanMapping whose len is constant
        then num is an integer, while num >= k -> O(1)
        """
        romanValue = ""
        intToRomanMapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        for k, v in intToRomanMapping.items():
            while num >= k:
                romanValue += v
                num -= k

        return romanValue

    # Similar solution
    def intToRoman(self, num: int) -> str:
        romanValue = ""
        intToRomanMapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        while num > 0:
            for k, v in intToRomanMapping.items():
                if num >= k:
                    romanValue += v
                    num -= k
                    break

        return romanValue


solution =  Solution()
assert solution.intToRoman(1994) == "MCMXCIV"
assert solution.intToRoman(3999) == "MMMCMXCIX"