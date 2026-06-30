import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        freq = {}
        heap = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        return [heapq.heappop(heap)[1] for i in range(k)]
            

