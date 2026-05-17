class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)            
            string += f"{length}@"
            string += word
        return string

    def decode(self, s: str) -> List[str]:
        ans = []
        total_len = ""
        temp_str = ""
        i = 0
        while i < len(s):
            # 1. Grab the length digits
            while s[i] != "@":
                total_len += s[i]
                i += 1
            
            # 2. STEP OVER THE "@" FIRST
            i += 1 
            num = i
            
            # 3. Grab the word
            while i < num + int(total_len):
                temp_str += s[i]
                i += 1
                
            # 4. Append correctly and RESET variables
            ans.append(temp_str)
            total_len = ""
            temp_str = ""
            
        return ans  # Return the final list of decoded strings