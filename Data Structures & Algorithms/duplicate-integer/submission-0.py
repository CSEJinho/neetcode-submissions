class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.num_lst = set()
        for self.num in nums:
            if self.num in self.num_lst:
                return True 
            else:
                self.num_lst.add(self.num)
        return False
            