class Solution:
    """
    brute force
    runtime: O(n^3)
    memory: O(n)
    """
    # def longestPalindrome(self, s):
    #     def isPalindrome(pali):
    #         middle = len(pali) // 2  # not len(pali) + 1 since we want the index
    #         if middle == 0: return True
    #
    #         if len(pali) % 2 == 1:
    #             # odd length word
    #             left = pali[0:middle]
    #             right = pali[middle + 1:]
    #         else:
    #             # even length word
    #             left = pali[0:middle]
    #             right = pali[middle:]
    #
    #         return left == right[::-1]
    #
    #     longest = ''
    #
    #     for i, char in enumerate(s):
    #         for j in range(i + len(longest) + 1, len(s) + 1):  # +1 since j is being used for string slices
    #             if isPalindrome(s[i:j]):
    #                 longest = s[i:j] if j - i > len(longest) else longest
    #     return longest

    """
    standard dp
    https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution/194444
    runtime: O(n^2)
    memory: O(n^2)
    """
    def longestPalindrome(self, s):
        table = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or table[i + 1][j - 1] == 1):
                    table[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j + 1]
                        max_length = j - i + 1
        return ans





if __name__ == '__main__':
    s = Solution()
    assert s.sol(1) == 1
