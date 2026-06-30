class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)

            if char == ')' and stack[len(stack) - 2] == '(':
                stack.pop()
                stack.pop()
                
            if char == ']' and stack[len(stack) - 2] == '[':
                stack.pop()
                stack.pop()
                
            if char == '}' and stack[len(stack) - 2] == '{':
                stack.pop()
                stack.pop()
            
            
            
    
        return len(stack) == 0