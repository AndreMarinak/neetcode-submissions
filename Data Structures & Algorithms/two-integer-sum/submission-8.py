class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dmaps={}

        for index, number in enumerate(nums):
            diff= target-number
            if diff in dmaps:
                return [dmaps[diff],index]
            else:
                dmaps[number]=index
