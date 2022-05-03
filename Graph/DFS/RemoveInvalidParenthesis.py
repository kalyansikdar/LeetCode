class Solution:
    def removeInvalidParentheses(self, s: str):
        # initialize a set with one element
        # set is used here in order to avoid duplicate element
        candidates = set([s])       # Creates a set with the input str as it's only element
        print (type(candidates), candidates)
        while True:
            valid = []
            for candidate in candidates:
                if self.isValid(candidate):     # Checks if the only element is valid, it's the answer as minimum
                    # number of paranthesis is to be removed.
                    valid.append(candidate)

            if valid:
                return valid
            # initialize an empty set
            new_candidates = set()
            # BFS - finds all the possible candidates, neglects the dups by using set
            for candidate in candidates:
                for i in range(len(candidate)):
                    new_candidates.add(candidate[:i] + candidate[i + 1:])
            candidates = new_candidates

    def isValid(self, candidate):
        open = 0
        for ch in candidate:
            if ch == '(':
                open += 1
            elif ch == ')':
                open -= 1
                if open < 0:
                    return False

        return open == 0


solution = Solution()
input_str = "()())()"
input_str = "(a)())()"
print(solution.removeInvalidParentheses(input_str))