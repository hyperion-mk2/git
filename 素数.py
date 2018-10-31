class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        buffdict = [0]*(n)
        if n == 1:
            return 0
        if n == 0 :
            return 0
        m = 2
        for index in range(2, int(n ** 0.5)+1):
            while index * m < n:
                buffdict[index * m] += 1
                m += 1
            m = 2
        return buffdict.count(0) - 2

if __name__ == '__main__':
    print(Solution.countPrimes(Solution,0))
