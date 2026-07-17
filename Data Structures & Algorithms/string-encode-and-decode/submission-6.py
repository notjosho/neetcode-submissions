class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}-{s}-"
        return result[:-1]

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 1
        result = []
        while j < len(s): 
            if s[j] != "-":
                j+=1
                continue
            lenstr = int(s[i:j])
            i = j + 1
            j = i + lenstr 
            word = s[i:j]
            result.append(word) 
            j += 1
            i = j
        return result
