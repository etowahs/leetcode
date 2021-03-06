class Solution:
    """
    Notes:
    merging two sorted arrays takes O(n + m) time, but we want to do better than linear time.
    1. extend one of the lists O(m), sort them O((n+m)log(n+m), get the median O(1)
    2. combine the lists O(m + n), get the median O(1)
    3.
    """

    """
    naive/dumb solution
    runtime: O((n+m)log(n+m))
    memory: O(n+m)
    """
    # def findMedianSortedArrays(self, nums1, nums2):
    #     nums1.extend(nums2)
    #     nums1.sort()
    #
    #     if len(nums1) == 1:
    #         return nums1[0]
    #
    #     middle = len(nums1) / 2
    #     if len(nums1) % 2:
    #         median = nums1[len(nums1) // 2]
    #     else:
    #         median = (nums1[(len(nums1) // 2) - 1] + nums1[(len(nums1) // 2)]) / 2
    #
    #     return median

    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        # always make it so that nums1 has the same or less elements as nums2
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax = 0, m
        half = (n + m + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i

            if i > 0 and nums1[i - 1] > nums2[j]:
                # need to decrease i
                imax = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                # need to increase i so that j is lower
                imin = i + 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (n + m) % 2:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([3], [1, 2]))
