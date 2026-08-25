class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        i = 0
        res = 0
        while i < len(nums):
            streak = 0
            curr = nums[i]
            while i < len(nums) and curr == nums[i]:
                i += 1
                curr += 1
                streak += 1
            res = max(res, streak)
        return res
            