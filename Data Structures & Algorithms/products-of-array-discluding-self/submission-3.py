class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        prod = 1
        for num in nums:
            if num != 0:
                prod *= num

        if zero_count == 1:
            result = [0] * len(nums)
            result[nums.index(0)] = prod
            return result

        return [prod//num for num in nums]
