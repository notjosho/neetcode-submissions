class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = ''.join(sorted(list(s)))
        t_array = ''.join(sorted(list(t)))
        return s_array == t_array