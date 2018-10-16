class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        s=0
        for i in range(l):
            s=max(s,i+nums[i])
            if s>=(l-1):
                return True
            if i==s:
                break
        return False
if __name__ == '__main__':
    print(Solution.canJump(Solution,[2,3,1,1,4]))