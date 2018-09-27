class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        indexnum = 0
        try:
            indexnum = haystack.index(needle)
        except:
            indexnum = -1
        return indexnum

if __name__ == "__main__":
    print(Solution.strStr(Solution,"3232","3333"))