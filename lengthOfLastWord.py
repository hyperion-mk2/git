class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s == ""):
            return 0
        alllength = len(s) - 1
        datanum = 0
        verb = 0
        charlist =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        for index in range(len(s)):
            if(verb == 1):
                if(charlist.count(s[alllength-index])>0):
                    datanum+=1
                    if (alllength == index):
                        return datanum
                else:
                    return datanum
            if(verb == 0 and charlist.count(s[alllength-index])>0):
                verb = 1
                datanum = 1

        return datanum





if __name__ == "__main__":
    print(Solution.lengthOfLastWord(Solution,"Hello World"))

