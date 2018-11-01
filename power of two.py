class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < -1:
            n = -n
        elif n <= 0:
            return False
        if n <= 2:
            return True
        while n > 2:
            if n % 2 != 0:
                return False
            n = n / 2
        return True

if __name__ == '__main__':
    print(Solution.isPowerOfTwo(Solution,16))