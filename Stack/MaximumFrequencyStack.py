class FreqStack:

    def __init__(self):
        self.freq = {}
        self.freqStack = {}
        self.maxFreq = 0

    def push(self, x: int) -> None:
        """
        Push
        1. Maintain two dict - One for freq mapping another for each freq maintain the elements inserted at that freq
        Like this -
        freq = {5: 3, 7: 2, 4: 1}
        freqStack = {1: [5, 7, 4], 2: [5, 7], 3: [5]} i.e. for 5,7 freq was updated to 1 then to 2, then for 5, it was
        updated to 3
        2. Maintain maxFreq
        3. When pushed update freq, add to stack for that freq, update maxFreq

        Pop:
        1. Get maxFreq element from freqStack, remove top element, if empty, then no need to handle this empty list
        anymore, so decrease maxFreq by 1. If there is no key after decreasing by one, then it returns an empty list,
        decrease again
        2. Decrease the freq of that element. It's needed because while pushing the freq is needed.
        https://www.youtube.com/watch?v=0fRmVjxopiE
        """
        if x not in self.freq:
            self.freq[x] = 1
        else:
            self.freq[x] += 1

        frequency = self.freq[x]
        if frequency > self.maxFreq:
            self.maxFreq = frequency

        if frequency not in self.freqStack:
            self.freqStack[frequency] = [x]
        else:
            self.freqStack[frequency].append(x)

    def pop(self) -> int:
        # get maxFreq element from freqStack, remove top element, if empty, remove the key
        # if key is removed, decrease maxFreq by 1
        stack = self.freqStack[self.maxFreq]
        top = stack.pop()
        if len(stack) == 0:
            self.maxFreq -= 1

        self.freq[top] -= 1

        return top

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()