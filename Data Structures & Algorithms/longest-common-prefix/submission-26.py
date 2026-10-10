class Solution:     
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = 200
        for s in strs:
            if len(s) < min :
                min = len(s)
        for i in range(0, min):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0][:min]