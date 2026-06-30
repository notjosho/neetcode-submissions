class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char not in hashMap:
                stack.append(char)
                continue
            elif not stack or stack[-1] != hashMap[char]:
                return False
            stack.pop()

        return len(stack) == 0