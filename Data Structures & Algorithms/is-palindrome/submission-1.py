class Solution:
    def isPalindrome(self, s: str) -> bool:
        # List comprehension to filter only alphanumeric chars and lower them
        cleaned_chars = [char.lower() for char in s if char.isalnum()]
        
        # Join list into a string
        cleaned_s = "".join(cleaned_chars)
        
        # Compare string to its reverse slice [::-1]
        return cleaned_s == cleaned_s[::-1]