class Solution:
    def findItinerary(self, tickets):
        """
        Algorithm Steps:
        1. Form adjacency list
        2. Sort the list lexically
        2. Push JFK into stack.
        3. While stack is not empty -
            a. take top element of stack and if it has adj locations, get first adj location, push into stack
            b. remove that location from adjList
            c. If it does not have adjLocations, delete that from stack and add to result
        4. Return the result in reverse order
        :param tickets:
        :return:
        """
        adjList = {}
        stack = []
        result = []

        for i in tickets:
            if i[0] not in adjList:
                adjList[i[0]] = []
            adjList[i[0]].append(i[1])

        print(adjList)
        for k, v in adjList.items():
            adjList[k].sort()

        print(adjList)

        stack.append("JFK")     # as per question, man starts from JFK always

        while stack:
            curr = stack[-1]

            if curr in adjList and len(adjList[curr]) > 0:
                listCurr = adjList[curr][0]
                stack.append(listCurr)
                adjList[curr].remove(listCurr)

            else:
                result.append(curr)
                del stack[len(stack) - 1]

        return result[::-1]


solution = Solution()
tickets = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"], ["ATL","JFK"], ["ATL","SFO"]]
print ('Result: ', solution.findItinerary(tickets))