class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = []
        buystack = []
        for index in range(len(prices)):
            if(index == len(prices)-1):
                if len(buystack) > 0:
                    profit.append(prices[index] - buystack[0])
                continue
            if(prices[index]<prices[index+1]):
                buystack.append(prices[index])
            if(prices[index]>prices[index+1] and len(buystack) > 0):
                profit.append(prices[index] - buystack[0])
                buystack = []
        profit.sort()
        return profit

if __name__ == '__main__':
    print(Solution.maxProfit(Solution,[1,2,4,2,5,7,2,4,9,0]))