class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buystack = []
        for index in range(len(prices)):
            if(index == len(prices)-1):
                if len(buystack) > 0:
                    profit += prices[index] - buystack[0]
                return profit
            if(prices[index]<prices[index+1]):
                buystack.append(prices[index])
            if(prices[index]>prices[index+1] and len(buystack) > 0):
                profit += prices[index] - buystack[0]
                buystack = []
        return profit


if __name__ == '__main__':
    Solution.maxProfit(Solution,[7,1,5,3,6,4])


