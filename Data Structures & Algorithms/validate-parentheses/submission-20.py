class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 and len(s) == 0:
            return False
        stack = [] 
        for i in range(len(s)):
            if s[i] == "(" :
                stack.append(")")
            elif s[i] == "{" :
                stack.append("}")
            elif s[i] == "[" :
                stack.append("]") 
            elif s[i] == ")" or s[i] == "}" or  s[i] == "]" :
                if len(stack) == 0 :
                    return False
                else :
                    if stack.pop() != s[i] :
                        return False
                    
        if len(stack) == 0 :
                return True
        return False 
