class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x
        return self.pow(self,x,n)

    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n>1 and n%2 == 0:
            return self.pow(self,x*x,n/2)
        if n%2 != 0:
            return self.pow(self,x*x,n//2)*self.pow(self,x,n%2)

if __name__ == '__main__':
    print(Solution.myPow(Solution,2.0,7))