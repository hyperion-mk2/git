class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # TODO multiply

    def plus(self,str1,str2):
        """

        :param str1: str
        :param str2: str
        :return: str
        """
        tstr = [0]*(max(len(str1),len(str2)))
        print(tstr)
        for index in range(1,min(len(str1),len(str2))+1):
            print(str1[-index])
            print(str2[-index])
            num =int(str1[-index]) +int(str2[-index])
            if num >= 10:
                tstr[-index] += (num - 10)
                if index == len(tstr):
                    tstr.insert(0,0)
                tstr[-(index+1)] += 1
            else:
                tstr[-index] += num
        str3 = [str(i) for i in tstr]

        return "".join(str3)

if __name__ == '__main__':
    print(Solution.plus(Solution,'623','456'))