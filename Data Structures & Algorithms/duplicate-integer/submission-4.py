class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            copied_nums = nums[:]
            copied_nums.pop(index)
            if num in copied_nums:
                return True
        return False