# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []

        list_of_pairs = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while(j >= 0 and pairs[i].key < pairs[j].key):
                pairs[j], pairs[i] = pairs[i], pairs[j]
                j-=1
                i-=1
                
            list_of_pairs.append(pairs[:])
        
        return list_of_pairs