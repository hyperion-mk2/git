class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deletenum = 0
        index = 0
        while index < len(nums) - 1:
            if(nums[index] == nums[index+1]):
                nums.pop(index)
                deletenum += 1
            else:
                index += 1
        return nums
if __name__ == "__main__":
    nums =[1,2,2,1,1]
    Solution.removeDuplicates(Solution, nums)
    print(nums)