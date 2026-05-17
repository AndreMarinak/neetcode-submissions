class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_words=[]
        for word in strs:
            sorted_chars = sorted(word)       # step 1: sort letters in the word
            sorted_words.append(''.join(sorted_chars))  # step 2: join the letters back into a string
        
        dic={}  
        for i in range (len(sorted_words)):
            if sorted_words[i] not in dic:
                dic[sorted_words[i]]=[strs[i]]
            else:
                dic[sorted_words[i]].append(strs[i])
        return list(dic.values())

                
