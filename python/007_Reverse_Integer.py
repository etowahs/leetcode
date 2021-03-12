class Solution:
    """
    naive solution
    runtime: O(n). String reversal takes O(n)
    memory: O(n)
    """
    def reverse(self, x):
        s = str(x)[::-1]
        if len(s) == 1:
            return int(s)
        if s[-1] == '-':
            s = ''.join(['-', s[:-1]])
        i = int(s)
        if i >= 2**31 or i < -2**31:
            return 0
        return i

if __name__ == '__main__':
    s = Solution()
