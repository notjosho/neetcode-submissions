class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while(i < len(s)):
            j = s.index("#", i)

            length = int(s[i:j])
            word = s[j+1:j+1+length]

            i = j+1+length
            result.append(word)
        
        return result
