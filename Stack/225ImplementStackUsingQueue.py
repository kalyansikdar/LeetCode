class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        """
        TC: O(N) as it's traversing over the first queue once, then again traversing queue2. So it's 2N ~ N
        """
        if len(self.queue1) == 0:
            return -1

        topElement = 0
        # pop(0) function pops from 0th index. pop() removes from end
        for i in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.pop(0))

        topElement = self.queue1.pop(0)

        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

        return topElement

    def top(self) -> int:
        return self.queue1[len(self.queue1) - 1]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()