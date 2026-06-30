class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = {}

        for i, char in enumerate(s):
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

        for char in t:
            if char in table:
                if table[char] == 1:
                    table.pop(char)
                else:
                    table[char] -= 1
            
        return len(table) == 0