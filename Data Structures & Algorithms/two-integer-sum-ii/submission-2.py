class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return[i+1,j+1]

"""        nums=numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]
        return []"""