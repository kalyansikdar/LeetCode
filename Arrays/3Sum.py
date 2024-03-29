class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()

        # we do not need to try the last 2 because there is no place to assign start and end
        for i in range(len(nums) - 2):
            # since the list is sorted, if any number is > 0, then all subsequent numbers would also be greater than 0,
            # adding with subsequent number never result to 0
            if nums[i] > 0:
                break

            # if number is same as previous, the conditions are already checked, hence skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]

                if total == 0:  # found!!
                    result.append([nums[i], nums[start], nums[end]])

                    # avoid duplicates
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1

                    start += 1
                    end -= 1

                elif total > 0:  # as the list is sorted, we need to try lesser numbers
                    end -= 1
                else:  # as the list is sorted, we need to try higher numbers
                    start += 1

        return result


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# Below example is for duplicate issue
nums = [-2, 0, 0, 2, 2]
assert solution.threeSum(nums) == [[-2, 0, 2]]
nums = [1, -1, -1, 0]
assert solution.threeSum(nums) == [[-1, 0, 1]]
nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
assert solution.threeSum(nums) == [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]]
nums = [-1, 0, 1, 2, -1, -4]
assert solution.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
