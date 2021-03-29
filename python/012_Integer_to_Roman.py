class Solution:
    """
    linear solution based stored values
    runtime: O(n)
    memory: O(1)
    """

    def intToRoman(self, num):
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for i in range(len(vals)):
            result += roman[i] * int(num / vals[i])
            num = num % vals[i]

        return result

if __name__ == '__main__':
    s = Solution()
