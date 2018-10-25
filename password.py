class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n != 0:
            if (n % 2 == 1):
                sum += 1
            n = n//2
        return sum

if __name__ == "__main__":
    print(Solution.hammingWeight(Solution,8))