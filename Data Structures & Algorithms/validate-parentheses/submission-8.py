class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        s = list(s)
        st1 = []
        count = 0
        # for p in s:
        #     if p == ")" or p == "}" or  p == "]" :
        #         count += 1
        # if count == 0 :
        #     return False
        for p in s:
            if p == "(" :
                st1.append(")") 
            elif p == "{" :
                st1.append("}") 
            elif p == "[" :
                st1.append("]") 
            else:
                if len(st1) != 0 and p == st1[-1]:
                    st1.pop()
                else:
                    return False
        if len(st1) >= 1:
            return False
        return True 