class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        returnnum = 0
        ysf = 9
        numlength = 0
        datalist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nulllength = len(str)
        for index in range(len(str)):
            if (str[index] != ' '):
                nulllength = index
                break
        str = str[nulllength:]
        if (str == ""):
            return 0

        if (str[0] == '-'):
            ysf = 0
        if (str[0] == '+'):
            ysf = 2
        if (datalist.count(str[0]) == 1):
            ysf = 1
        strlist = list(str)
        numlength = len(strlist)
        for index in range(len(strlist) - 1):
            if (datalist.count(strlist[index + 1]) == 0):
                numlength = index + 1
                break
        newstr = "".join(strlist)[:numlength]
        if (ysf == 1):
            for index in range(len(newstr)):
                returnnum += (10 ** (len(newstr) - index - 1)) * datalist.index(newstr[index])

        if (ysf == 0):
            for index in range(len(newstr) - 1):
                returnnum -= (10 ** (len(newstr) - index - 2)) * datalist.index(newstr[index + 1])
        if (ysf == 2):
            for index in range(len(newstr) - 1):
                returnnum += (10 ** (len(newstr) - index - 2)) * datalist.index(newstr[index + 1])

        if (returnnum < -2147483648):
            returnnum = -2147483648
        if (returnnum > 2147483647):
            returnnum = 2147483647
        return returnnum
if __name__ == "__main__":
    print(Solution.myAtoi(Solution,"  823213"))