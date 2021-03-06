class Solution:
    # Number of non-empty substrings: n + n-1 + n-2 + n-3... 2, 1 = n(n+1)/2
    """
    naive solution
    runtime: O(n^2) 6.51%
    memory: O(n) but the set gets redefined with each iteration of loop so probably more
    """
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest = 0
    #     for i in range(len(s)):
    #         curr = set()
    #         for j in range(i, len(s)):
    #             if s[j] not in curr:
    #                 curr.add(s[j])
    #             else:
    #                 break
    #             longest = max(longest, len(curr))
    #     return longest

    """
   One pass sliding window
   runtime: O(n) 78.76%
   memory: O(n) 82.54%
   """
    # def lengthOfLongestSubstring(self, s):
    #     d = {}
    #     l, r = 0, 1
    #     longest = 0
    #     for i, c in enumerate(s):
    #         if c in d and d[c] >= l:
    #             l = d[c] + 1
    #         d[c] = i
    #         longest = max(longest, r - l)
    #         r += 1
    #     return longest
    """
   One pass sliding window, cleaner 
   runtime: O(n) 86.04%
   memory: O(n) 94.27%
   """
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        longest = 0
        for i, c in enumerate(s):
            if c in d and d[c] >= l:
                l = d[c] + 1
            d[c] = i
            longest = max(longest, i - l + 1)
        return longest


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring(" ") == 1
