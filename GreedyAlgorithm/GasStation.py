class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        startIdx = 0
        fuelBalance, deficit = 0, 0

        for i in range(len(gas)):
            fuelBalance += gas[i] - cost[i]  # accumulate the fuel balance if it's feasible to go

            if fuelBalance < 0:  # it's not possible to start from i
                deficit += fuelBalance  # in case it's not feasible, accumulate the deficit
                startIdx = i + 1  # as i cannot be the start index, setting i+1 as the possible start index
                fuelBalance = 0  # making it zero as this iteration did not contribute positively

        if fuelBalance + deficit >= 0:
            return startIdx
        else:
            return -1


solution = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(gas, cost))