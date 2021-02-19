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

        print (intermediate_result, open)

        result = ""

        for i in range(len(intermediate_result) - 1, -1, -1):
            if intermediate_result[i] == '(' and open > 0:
                open -= 1
                continue
            result += intermediate_result[i]

        return result[::-1]

    def minRemoveToMakeValid_better(self, s: str) -> str:
        """
        Algorithm:
        1. Covert the string to a list so that we can modify the index, because string is immutable (can't change)
        2. While looping thru the list, if a char is ( add the index to the stack
        3. If the char is closing bracket - ), then if openStack has some value, pop it (the open one is it's counter-part)
        4. If openStack does not have a value, means, the closing stack is before any open parentheses,
        hence it's unwanted. so update it to ''
        5. If any element left in openStack mean there are those number of excess pen parentheses, update those to ''
        6. Join the list elements to create string and return
        :param s:
        :return:
        """
        # error checking
        if not s:
            return ''

        # create a list and stack
        sList = list(s)
        openParenthesesStack = []

        # loop thru the input string and check for parentheses
        for idx, ch in enumerate(s):
            if ch == '(':
                openParenthesesStack.append(idx)

            if ch == ')':
                if openParenthesesStack:
                    openParenthesesStack.pop()
                else:
                    sList[idx] = ''

        # check stack for excess open parentheses and remove them
        while openParenthesesStack:
            idx = openParenthesesStack.pop()
            sList[idx] = ''

        # join the list to form a string and return
        return "".join(sList)


solution = Solution()
s = "())()((("
s = "()((()))"
# s = "(a(b(c)d)"
print (solution.minRemoveToMakeValid_better(s))