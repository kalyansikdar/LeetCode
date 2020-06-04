class Solution:
    def twoCitySchedCost(self, costs) -> int:
        if not costs:
            return None
        costDiff = {}
        minimumCost = 0

        for i in range(len(costs)):
            costDiff[i] = costs[i][1] - costs[i][0]

        sorted_costDiff = sorted(costDiff.items(), key=lambda kv: kv[1], reverse=True)

        serial = [i[0] for i in sorted_costDiff]

        i = 0
        while i < len(serial) // 2:
            minimumCost += costs[serial[i]][0]
            i += 1

        while i < len(serial):
            minimumCost += costs[serial[i]][1]
            i += 1

        return minimumCost


solution = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print (solution.twoCitySchedCost(costs))