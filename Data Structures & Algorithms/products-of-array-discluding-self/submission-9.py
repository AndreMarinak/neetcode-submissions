class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        zero_count = 0
        total_product_without_zeros = 1
    
        for num in nums:# Step 1: Count the zeros and find the product of all non-zero numbers
            if num == 0:
                zero_count += 1
            else:
                total_product_without_zeros *= num
        
        ans = []
        
        # Step 2: Build the answer array based on how many zeros were found
        for num in nums:
            # Case 1: More than one zero means every position is multiplied by a zero
            if zero_count > 1:
                ans.append(0)
                
            # Case 2: Exactly one zero in the array
            elif zero_count == 1:
                if num == 0:
                    # The zero gets the product of all other numbers
                    ans.append(total_product_without_zeros)
                else:
                    # Everything else gets wiped out by that single zero
                    ans.append(0)
                    
            # Case 3: No zeros at all, perfectly safe to divide
            else:
                # Using '//' ensures integer output instead of floats
                ans.append(total_product_without_zeros // num)
        
        return ans
