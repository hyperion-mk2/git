class Solution:
    numlist = []
    fulllist = []
    list0 = ['*']
    list1 = ['a', 'b', 'c']
    list2 = ['d', 'e', 'f']
    list3 = ['g', 'h', 'i']
    list4 = ['j', 'k', 'l']
    list5 = ['m', 'n', 'o']
    list6 = ['p', 'q', 'r', 's']
    list7 = ['t', 'u', 'v']
    list8 = ['w', 'x', 'y', 'z']
    list = [list0, list1, list2, list3, list4, list5, list6, list7, list8]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.des(self,0,digits)
        return self.fulllist
    def des(self,num,digits):
        if (num == len(digits)):
            self.fulllist.append(''.join(self.numlist))
            return 0
        if (digits[num] == '1'):
            if len(self.numlist) < num:
                self.numlist.append('*')
            else:
                self.numlist.insert(num, '*')
            self.des(self,num+1,digits)
        else:
            if len(self.numlist) <= num:
                self.numlist.append(self.list[int(digits[num])-1][0])
            else:
                self.numlist[num]=self.list[int(digits[num])-1][0]
            self.des(self,num+1,digits)
            if len(self.numlist) <= num:
                self.numlist.append(self.list[int(digits[num]) - 1][1])
            else:
                self.numlist[num] = self.list[int(digits[num]) - 1][1]
            self.des(self, num + 1, digits)
            if len(self.numlist) <= num:
                self.numlist.append(self.list[int(digits[num])-1][2])
            else:
                self.numlist[num] = self.list[int(digits[num]) - 1][2]
            self.des(self,num+1,digits)


if __name__ == "__main__":
        Solution.letterCombinations(Solution,'123')
        print(Solution.fulllist)