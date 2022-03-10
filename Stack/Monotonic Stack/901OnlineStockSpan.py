class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        """
        Algorithm:
        1. whenever the stack is empty, push index and price, return index + 1 -> no other price is smaller than that
        2. If the stack is not empty, check if the price is >= top price, if yes, pop from stack
        3. If stack is empty, again return index + 1 -> no other price is greater than that
        4. After popping if the stack is not empty, return (current index - topIndex) -> these many items are smaller
        than the current item. Also, store the item into stack

        """
        self.index += 1

        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()

        if not self.stack:
            self.stack.append((self.index, price))
            return self.index + 1

        topIndex = self.stack[-1][0]
        self.stack.append((self.index, price))

        return self.index - topIndex

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
