class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0

        dpi = [[0 for i in range(m)] for j in range(n)]
        dpi[0][0] = 1
        for index in range(0,n):
            for index2 in range(0,m):
                if index < n-1:
                    dpi[index+1][index2] += dpi[index][index2]
                if index2 < m-1:
                    dpi[index][index2+1] += dpi[index][index2]
        return dpi[-1][-1]
if __name__ == '__main__':
    print(Solution.uniquePaths(Solution,2,3))

