class Solution:
    """
    naive solution. Turn into string O(n) and compare pairs O(n/2)
    runtime: O(n)
    memory: O(n)
    """
    def isPalindrome(self, x):
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
