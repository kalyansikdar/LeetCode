class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n

        while m >= 1 and n >= 1:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[end - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[end - 1] = nums2[n - 1]
                n -= 1

            end -= 1

        if n != 0:
            for i in range(n):
                nums1[i] = nums2[i]