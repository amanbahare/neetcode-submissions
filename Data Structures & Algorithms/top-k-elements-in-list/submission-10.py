class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        arr = []
        output = []
        for key, value in my_dict.items():
            arr.append([value, key])
        arr.sort(reverse= True)
        for i in range(0, k):
            output.append(arr[i][1])
        return output