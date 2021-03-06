class Solution:
    """
    naive solution, literally makes a zigzag in a 2d list
    runtime: O(n)
    memory: O(numRows * n)
    """
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        elif numRows == 2:
            zigzag = [[''] * (len(s) + 1 // 2) for i in range(2)]
            j = 0
            for i, c in enumerate(s):
                zigzag[i % 2][j] = c
                if i % 2: j += 1
        else:
            zigzag = [[''] * (len(s) + 1 // 2) for i in range(numRows)]
            j, k = 0, 0
            zig = True  # always start in a zig
            for i, c in enumerate(s):
                zigzag[j][k] = c
                if zig and j < numRows - 1:
                    j += 1
                elif j == numRows - 1 or (not zig and j > 0):
                    zig = False
                    j -= 1
                    k += 1
                elif j == 0:
                    zig = True
                    j += 1

        combined = ''
        for row in zigzag:
            combined += ''.join(row)
        return combined

    """
    Optimized version, don't represent whole table including empty spaces, but just letters for each row
    runtime: O(n)
    memory: O(n)
    """

    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        table = [''] * numRows
        step = 1
        i = 0
        for c in s:
            table[i] += c
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step

        return "".join(table)

if __name__ == '__main__':
    s = Solution()
