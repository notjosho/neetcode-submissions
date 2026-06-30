class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            count_of_chars = [0] * 26
            for char in word:
                count_of_chars[ord(char) - ord('a')] += 1

            hash_map[tuple(count_of_chars)].append(word)

        return hash_map.values()