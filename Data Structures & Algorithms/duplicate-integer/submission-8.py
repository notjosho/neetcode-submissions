class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for i, num in enumerate(nums):
            if num in table:
                return True
            table[num] = i
        return False 
            