class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char not in hashMap:
                stack.append(char)
                continue
            elif char in hashMap and len(stack) > 0 and hashMap[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        print(stack)
        return len(stack) == 0