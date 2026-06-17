class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                pass
            seen.add(num)
        unique = set(nums)
        return(len(nums)!=len(seen))