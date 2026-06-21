class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. Pre-allocate ONLY the output array
        # This does not count against our space complexity!
        ans = [1] * n
        
        # 2. Build the prefix (left) products directly inside `ans`
        total = 1
        for i in range(n):
            ans[i] = total
            total *= nums[i]
            
        # 3. Calculate postfix (right) dynamically and multiply in-place
        total = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * total  # Multiply the existing prefix by the postfix
            total *= nums[i]         # Update the running postfix total
            
        return ans