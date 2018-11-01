class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = set()
        t.add(n)
        while n != 1:
            sum = 0
            m = str(n)
            for index in range(len(m)):
                sum += int(m[index])**2
            n = sum
            if n in t:
                return False
            else:
                t.add(n)
        return True


if __name__ == '__main__':
    print(Solution.isHappy(Solution,798))