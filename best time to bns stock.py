class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = []
        pricesstack = []
        change = 0
        index = 0
        while index < len(prices)-1:
            if(prices[index+1]>prices[index]):
                for index2 in range(index,len(prices)):
                    stack.append(prices[index2])
                    if(index2 == len(prices)-1):
                        change = 0
                        pricesstack.append(stack[-1] - stack[0])
                        stack = []
                        continue
                    if(prices[index2+1]<prices[index2]):
                        pricesstack.append(stack[-1]-stack[0])
                        if change != 1:
                            index = index2
                            change = 1
            index = index+1
        if(pricesstack == None):
            return 0
        pricesstack.sort()
        return pricesstack[-1]

if __name__ == '__main__':
    print(Solution.maxProfit(Solution,[7,6,4,3,1]))