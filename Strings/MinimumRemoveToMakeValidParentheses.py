class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Step 1: Check if each ch is "(", increase counter
        Step 2: if ch is ")", decrease counter to balance parenthesis but if parenthesis are already balanced, skip
        Step 3: Add filtered ch to a string - intermediate_result
        Step 4: intermediate_result may have "(" at the end which was not handled
        Step 5: Loop from end to filter the "(" and store ch into result
        Step 6: return result after reversing as in step 5 loop ran from end
        :param s:
        :return:
        """
        open = 0
        intermediate_result = ""

        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                if open == 0:
                    continue
                open -= 1

            intermediate_result += ch

        result = ""

        for i in range(len(intermediate_result) - 1, -1, -1):
            if intermediate_result[i] == '(' and open > 0:
                open -= 1
                continue
            result += intermediate_result[i]

        return result[::-1]


solution = Solution()
s = "())()((("
print (solution.minRemoveToMakeValid(s))