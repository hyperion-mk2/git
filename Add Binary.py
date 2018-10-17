class Solution:
    def addBinary(self,str1,str2):
        """

        :param str1: str
        :param str2: str
        :return: str
        """
        tstr = [0]*(max(len(str1),len(str2)))
        print(tstr)
        for index in range(1,min(len(str1),len(str2))+1):
            num =int(str1[-index]) +int(str2[-index]) + tstr[-index]
            if num >= 2:
                tstr[-index] = (num - 2)
                if index == len(tstr):
                    tstr.insert(0,0)
                tstr[-(index+1)] += 1
            else:
                tstr[-index] = num

        for index in range(min(len(str1),len(str2))+1,max(len(str1),len(str2))+1):
            if len(str1)>=len(str2):
                num = int(str1[-index])+ tstr[-index]
                if num >= 2:
                    tstr[-index] = (num - 2)
                    if index == len(tstr):
                        tstr.insert(0, 0)
                    tstr[-(index + 1)] += 1
                else:
                    tstr[-index] = num
            else:
                num = int(str2[-index]) + tstr[-index]
                if num >= 2:
                    tstr[-index] = (num - 2)
                    if index == len(tstr):
                        tstr.insert(0, 0)
                    tstr[-(index + 1)] += 1
                else:
                    tstr[-index] = num
        str3 = [str(i) for i in tstr]
        return "".join(str3)

if __name__ == '__main__':
    print(Solution.addBinary(Solution, '11', '1'))