class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        correct = {}

        # 1. Count frequencies
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    
        # 2. Group numbers by their frequency (Buckets)
        for num, occr in freq.items():
            if occr in correct:
                correct[occr].append(num)
            else:
                correct[occr] = [num]

        res = [] # Fix 1: Initialize res
        
        # Fix 3: Start from the maximum possible frequency, count down to 1
        for i in range(len(nums), 0, -1):
            # Fix 2: Check if this frequency bucket exists in 'correct'
            if i in correct:
                for num in correct[i]: 
                    res.append(num)
                    if len(res) == k:
                        return res