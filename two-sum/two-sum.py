class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for a in range(i+1, len(nums)):
                sum = nums[i] + nums[a]
                if sum == target:
                    return [i,a]
        