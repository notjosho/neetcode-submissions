class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        zero_idx = None
        result = []
        for idx, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_idx = idx

        if zero_count > 1:
            return [0 for i in nums]
        elif zero_count == 1:
            for num in nums:
                if num != 0:
                    product *= num
            result = []
            for i in range(len(nums)):
                if i != zero_idx:
                    result.append(0)
                    continue
                result.append(product)
            return result

        for num in nums:
            product *= num

        for num in nums:
            if num == 0:
                result.append(int(product))
                continue
            result.append(int(product/num))

        return result
