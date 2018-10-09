class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        alllength = len(digits) - 1
        for index in range(len(digits)+1):
            if (index == alllength + 1):
                digits.insert(0,0)
                alllength += 1
            num = digits[alllength-index] + 1
            if(num == 10):
                digits[alllength - index] = 0
            else:
                digits[alllength - index] = num
                return digits


if __name__ == "__main__":
    print(Solution.plusOne(Solution,[9,9,9,9]))
