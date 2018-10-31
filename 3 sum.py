class Solution:
    def twoSum(self, nums, target,leftnum):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <=1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if i == leftnum:
                continue
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        leftnum = 0
        numstack = []
        for index in range(len(nums)):
            numstack.append(self.twoSum(Solution,nums,-nums[index],index))
        return numstack

if __name__ == '__main__':
    print(Solution.threeSum(Solution,[-1, 0, 1, 2, -1, -4]))