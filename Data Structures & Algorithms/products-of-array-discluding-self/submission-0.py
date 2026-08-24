class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        output = []
        for num in nums:
            prod *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                prodz = 1
                for j in range(len(nums)):
                    if j == i: continue
                    prodz *= nums[j]
                output.append(int(prodz))
            else:
                output.append(int(prod/nums[i]))
        return output