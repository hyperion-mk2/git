import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0
        if(0<x<4):
            return 1
        numleft = 2
        numright = x//2
        while (numleft<=numright):
            numleft = 2 * numleft
            numright = numright // 2
        newtonx = numright
        for index in range(int(math.log(numleft,10))+1):
            newtonx = (newtonx+x/newtonx)/2

        return int(newtonx)
if __name__ == "__main__":
    print(Solution.mySqrt(Solution,2147395599))