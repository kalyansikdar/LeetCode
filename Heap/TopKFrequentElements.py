import heapq
import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        frequencyMap = collections.Counter(nums)
        heap = []
        heapq.heapify(heap)
        print (frequencyMap)
        for key, val in frequencyMap.items():       # O(n) for loop
            # here while inserting into heap, value is the key, hence the elements will be ordered based on value
            # which is the frequency of occurrence
            heapq.heappush(heap, (val, key))        # while push val is the key as min heap will arrange the heap
            # based on frequency
            # heap push - O(logn), pop - O(logn)
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
        print ('heap: ', heap)
        result = []
        while len(heap) > 0:
            result.append(heapq.heappop(heap)[1])

        return result


solution = Solution()
nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
nums1 = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums1, k))
