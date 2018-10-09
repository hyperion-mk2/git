class Solution:
    data = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        if(n!=0):
            if(n>2):
                if(n in self.data):
                    return self.data[n]
                else:
                    self.data[n] = self.climbStairs(self,n - 1) + self.climbStairs(self,n - 2)
                return self.data[n]

            if(n == 2):
                return 1 + self.climbStairs(self,n - 1)
            if(n == 1):
                return 1
        else:
            return 0
if __name__ == "__main__":
    print(Solution.climbStairs(Solution,35))