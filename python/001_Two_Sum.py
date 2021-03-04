class Solution:
    """
    nested loops
    runtime: 36 ms, O(n(n+1)/2) = O(n^2)
    memory: 14.5 MB, O(1)
    """
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #
    #     return []
    """
    one pass hash
    runtime: 48 ms, O(n)
    memory: 14.4 MB, O(n)
    """
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
        return []


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([1, 2, 3], 3) == [0, 1]
    assert s.twoSum([1, 10, 100, 1000], 1001) == [0, 3]
    assert s.twoSum([1, 10, 100, 1000], 11) == [0, 1]