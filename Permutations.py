class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        index  = 0
        n = nums.count(2)
        m = 0
        while index < len(nums):
            if nums[index] == 0:
                del nums[index]
                nums.insert(0,0)
                index += 1
            elif nums[index] == 2:
                del nums[index]
                nums.append(2)
                m += 1
            elif nums[index] == 1:
                index += 1
            if m > n:
                return nums
        return nums

if __name__ == '__main__':
    print(Solution.sortColors(Solution,[1,2,0]))