class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        last_seen = {}  # maps char to its last index
        total_length = 0
        temp_length = 0
        start = 0  # start index of current window

        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                # char is repeated within current window
                start = last_seen[char] + 1
                temp_length = i - start + 1
            else:
                temp_length += 1

            last_seen[char] = i
            total_length = max(total_length, temp_length)

        return total_length