class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[m] = nums2[m]

        end = len(nums1) - 1  # nums1 is always bigger
        m, n = m - 1, n - 1

        while m >= 0 and n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[end] = nums2[n]
                n -= 1
            else:
                nums1[end] = nums1[m]
                m -= 1
            end -= 1

        print(nums1)
        return nums1


solution = Solution()
result = solution.merge([1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
# assert solution.merge([1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
# assert solution.merge([2,0], 1, [1], 1) == [1,2]
