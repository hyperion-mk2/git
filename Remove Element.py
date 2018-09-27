class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            if(nums[index] == val):
                nums.pop(index)
            else:
                index+=1

        return len(nums)


if __name__ == "__main__":
    nums =[-2,1,-3,4,-1,2,1,-5,4]
    val = -2
    print(Solution.removeElement(Solution, nums,  val))
    print(nums)