class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            if ((nums[index]>=0 and nums[index + 1]>=0) or (nums[index]<0 and nums[index + 1]<0)):
                nums[index] += nums[index + 1]
                nums.pop(index+1)
            else:
                index += 1
        index = 0
        if(nums[0] < 0):
            nums.pop(0)
        sumnums =[]+nums
        while len(nums) > 3:

            for index in range(len(nums)//2):
                nums[index] += nums[index + 1]
                nums.pop(index+1)
            sumnums = sumnums + nums
        return max(sumnums)

if __name__ == "__main__":
    nums =[-2,1,-3,4,-1,2,1,-5,4]
    print(Solution.maxSubArray(Solution, nums))