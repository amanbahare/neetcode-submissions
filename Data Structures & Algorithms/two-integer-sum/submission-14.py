class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            if nums[i] in seen:
                    return [seen[nums[i]],i]
            if nums[i] not in seen:
                seen[target - nums[i]] = i
            