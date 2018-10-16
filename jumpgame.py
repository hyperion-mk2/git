class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        nums1 = nums.copy()
        for index in range(len(nums1)-1):
            nums1[index+1] = 0
        for index in range(len(nums)-1):
            for index2 in range(nums[index]):
                if index2 + index < len(nums) - 1:
                    nums1[index2+1+index] += 1
        return nums1.count(0) ==0


if __name__ == '__main__':
    print(Solution.canJump(Solution,[2,0,0]))