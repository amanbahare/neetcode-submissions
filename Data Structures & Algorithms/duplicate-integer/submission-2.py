class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = []
        for i in range(0, len(nums)):
            if nums[i] not in store:
                store.append(nums[i])
            else:
                return True
        return False


