class Solution:
    def merge(self, intervals):
        """
        Time complexity: O(nlogn) for sorting + O(n) for while loop. Overall: O(nlogn)
        :param intervals:
        :return:
        """
        intervals = sorted(intervals, key=lambda kv: kv[0])     # list needs to be sorted so that all element can be
        # checked in O(N) later. However, sorting is NLogN here
        i = 1

        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][0] = min(intervals[i - 1][0], intervals[i][0])
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])

                del intervals[i]
            else:
                i += 1

        return intervals


solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print (solution.merge(intervals))