class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash_map = {}
        t_hash_map = {}
        for char in s:
            if char in s_hash_map:
                s_hash_map[char] += 1
            else:
                s_hash_map[char] = 0

        for char in t:
            if char in t_hash_map:
                t_hash_map[char] += 1
            else:
                t_hash_map[char] = 0

        return s_hash_map == t_hash_map                                                   