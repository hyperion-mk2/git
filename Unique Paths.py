class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if(m==1 and n==1):
            return 1
        elif(m==1):
            return self.uniquePaths(self,m, n-1 )
        elif(n==1):
            return self.uniquePaths(self,m - 1, n)
        else:
            return self.uniquePaths(self,m, n - 1) + self.uniquePaths(self,m - 1, n)


if __name__ == '__main__':
    print(Solution.uniquePaths(Solution,3,2))
