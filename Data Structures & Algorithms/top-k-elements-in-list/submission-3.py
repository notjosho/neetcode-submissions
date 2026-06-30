class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        
        for key, count in freq.items():
            buckets[count].append(key)

        for i in range(len(buckets)-1, 0, -1):
            if k == 0:
                break

            if len(buckets[i]) == 0:
                continue
            
            for bucket in buckets[i]:
                result.append(bucket)
                k -= 1

        return result