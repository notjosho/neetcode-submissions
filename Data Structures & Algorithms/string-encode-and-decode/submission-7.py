class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}-{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        result = []
        while i < len(s): 
            if s[j] != "-":
                j+=1
                continue
            print(f"lenstr->{s[i:j]}")
            lenstr = int(s[i:j])
            i = j + 1
            j = i + lenstr
            print(f"i->{i}")
            word = s[i:j]
            print(f"word->{word}")
            i = j 
            result.append(word)
        return result
