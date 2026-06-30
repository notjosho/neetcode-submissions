class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        for i in range(len(nums)):
            if nums[i] in solutions:
                index = solutions.index(nums[i])
                return [index, i]
            solutions.append(target - nums[i])
            print(solutions)
        return []