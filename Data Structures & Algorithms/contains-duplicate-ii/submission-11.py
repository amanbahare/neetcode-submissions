class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # Step 1: Har number ke saare indices store karo
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = [i]
            else:
                dict1[nums[i]].append(i)
        
        # Step 2: Sirf wo numbers rakho jo 2+ baar aaye
        dict2 = {}
        for key, value in dict1.items():
            if len(value) >= 2:
                dict2[key] = value
        
        # Step 3: Har number ke consecutive indices check karo
        for indices in dict2.values():
            for i in range(len(indices) - 1):
                if abs(indices[i] - indices[i + 1]) <= k:
                    return True
        
        return False




