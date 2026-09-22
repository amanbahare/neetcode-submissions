class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {} 
        output = []
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else :
                dict1[num] += 1
        sorted_by_values = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        output = list(sorted_by_values.keys())[:k]
        return output