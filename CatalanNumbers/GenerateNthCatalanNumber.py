class CatalanNumbers:
    def __init__(self):
        pass

    def generateCatalanNumber(self, n):
        tracker = [0] * (n+1)
        return self.calculateCatalanNumber(n, tracker)

    def calculateCatalanNumber(self, n, tracker):
        """
        This is recursive algorithm
        """
        if tracker[n]:
            return tracker[n]

        local_result = 0
        if n <= 1:
            return 1
        else:
            for i in range(n):
                local_result += self.calculateCatalanNumber(i, tracker) * self.calculateCatalanNumber(n - i - 1, tracker)
            tracker[n] = local_result

        return local_result

    def calculateCatalanNo_DP(self, n):
        """
        DP solution:
        Space complexity O(N) -> Because of extra space in tracker
        Time complexity 0(N^2) -> O(N) for each loop
        """
        tracker = [0] * (n+1)
        tracker[0] = tracker[1] = 1

        for i in range(2, n+1):
            tracker[i] = 0

            for j in range(i):
                tracker[i] += tracker[j]*tracker[i-j-1]

        return tracker[n]


catalan = CatalanNumbers()
print(catalan.generateCatalanNumber(4))
print(catalan.calculateCatalanNo_DP(4))
