class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        third = []
        for index in range(len(nums)):
            if(len(third) == 0):
                third.append(nums[index])
            elif(len(third) == 1):
                if third[-1] < nums[index]:
                    third.append(nums[index])
                elif third[-1] > nums[index]:
                    third.insert(0,nums[index])
            elif(len(third) == 2):
                if third[-1] < nums[index]:
                    third.append(nums[index])
                elif third[-1] > nums[index] and third[0] < nums[index]:
                    third.insert(1,nums[index])
                elif third[0] > nums[index]:
                    third.insert(0, nums[index])
            elif(len(third) == 3):
                 for index2 in range(1,4):
                    if third[-index2] < nums[index]:
                        third.insert(4-index2,nums[index])
                        third.pop(0)
                        break
                    if third[-index2] == nums[index]:
                        break
        print(third)
        if(len(third)<3):
            return third[-1]
        else:
            return third[0]


if __name__ == '__main__':
    print(Solution.thirdMax(Solution,[1,2,2,5,3,5]))