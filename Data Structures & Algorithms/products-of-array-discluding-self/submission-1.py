class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n
        product = 1
        for i in range(n):
            prefix[i] = product
            product *= nums[i]
        product = 1
        for i in range(n)[::-1]:
            suffix[i] = product
            product *= nums[i]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

