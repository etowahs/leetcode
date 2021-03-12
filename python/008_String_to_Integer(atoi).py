class Solution:
    """
    naive solution. Looks for whitespace, then +/-, then digits
    runtime: O(n)
    memory: O(n)
    """
    def myAtoi(self, s):
        i = 0
        sign = 1
        if len(s) == 0: return 0
        # get whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        # get signs
        if i < len(s):
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                sign = 1
                i += 1
        else:
            return 0

        if i >= len(s) or not s[i].isdigit():
            return 0
        else:
            # get digits
            digits = 0
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                digits = (digits * 10) + int(s[i])
                i += 1

            num = sign * digits
            if num >= 2 ** 31:
                return 2 ** 31 - 1
            elif num < -2 ** 31:
                return -2 ** 31
            else:
                return num

if __name__ == '__main__':
    s = Solution()
