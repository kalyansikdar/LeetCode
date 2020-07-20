class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currPosition = 0
        self.logicalEnd = 0     # maintains the logical end

    def visit(self, url: str) -> None:
        self.currPosition += 1
        if self.currPosition == len(self.history):
            self.history.append(url)
        else:
            self.history[self.currPosition] = url       # discard forward history
        self.logicalEnd = self.currPosition         # current becomes the logical end

    def back(self, steps: int) -> str:
        self.currPosition = max(0, self.currPosition - steps)       # if current - steps < 0, you cannot go backward
        # than index 0
        return self.history[self.currPosition]

    def forward(self, steps: int) -> str:
        self.currPosition = min(self.currPosition + steps, self.logicalEnd)
        return self.history[self.currPosition]


solution = BrowserHistory("leetcode.com")
print (solution.visit("google.com"), end=" ")
print (solution.visit("facebook.com"), end=" ")
print (solution.visit("youtube.com"), end=" ")
print (solution.back(1), end=" ")
print (solution.back(1), end=" ")
print (solution.forward(1), end=" ")
print (solution.visit("linkedin.com"), end=" ")
print (solution.forward(2), end=" ")
print (solution.back(2), end=" ")
print (solution.back(7), end=" ")
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

# Answer:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]