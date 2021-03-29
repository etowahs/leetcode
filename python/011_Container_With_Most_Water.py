class Solution:
    """
    naive solution
    runtime: O(n^2)
    memory: O(1)
    """
    def maxArea(self, height):
        biggest = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                biggest = max(biggest, (j - i) * (min(height[i], height[j])))

        return biggest

    """
    two pointer solution
    based on https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
    runtime: O(n)
    memory: O(1)
    """
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        volume = 0

        while left < right:
            volume = max(volume, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return volume

if __name__ == '__main__':
    s = Solution()
