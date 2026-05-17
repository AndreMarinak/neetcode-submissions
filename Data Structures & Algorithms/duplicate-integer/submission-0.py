class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst=[]
        for num in nums:
            if num in lst:
                return True
            else:
                lst+=[num]
        return False