class Solution:
    def romanToInt(self, s: str) -> int:
        intVal = 0
        # error checking
        if not s:
            return 0

        # Store mapping
        valueMappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Loop over the input and compare each roman letter from mappings. If it's greater than OR equal to the next
        # add the value to intVal, else subtract the value from intVal
        for i in range(len((s)) - 1):
            if valueMappings[s[i]] >= valueMappings[s[i + 1]]:
                intVal += valueMappings[s[i]]
            else:
                intVal -= valueMappings[s[i]]

        # add the last letter to intVal
        intVal += valueMappings[s[-1]]

        return intVal


solution = Solution()
s = "MCMXCIV"
assert solution.romanToInt(s) == 1994
s = "LVIII"
assert solution.romanToInt(s) == 58