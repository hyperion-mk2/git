class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        data = "1"
        chi  = '1'
        chn = 0
        if (n == 1):
            return data
        for index in range(n-1):
            newdata = ""
            for index in range(len(data)):
                if (data[index] == chi):
                    chn +=1
                else:
                    newdata = newdata + str(chn) + chi
                    chi = data[index]
                    chn = 1
                if (index == len(data)-1):
                    newdata = newdata + str(chn) + chi
                    chi = newdata[0]
                    chn = 0
            data = newdata
        return data
if __name__ == "__main__":
    print(Solution.countAndSay(Solution,5))
