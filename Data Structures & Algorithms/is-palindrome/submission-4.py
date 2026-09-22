class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        temp1 = ""
        s = s.lower()
        for i in range(len(s)-1,-1,-1):
            if (s[i].isdigit() or s[i].isalpha()):
                temp+=s[i]
        for i in range(len(s)):
            if s[i].isdigit() or s[i].isalpha():
                temp1+=s[i] 
        print("temp : ",temp)
        print("temp1 : ",temp1)
        if temp == temp1:
            return True
        return False

                
                
