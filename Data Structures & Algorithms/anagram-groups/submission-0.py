class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]:
            return [[""]]

        dictn={}
        lst=[]
        for word in strs:
            new="".join(sorted(word))
            if new in dictn:
                dictn[new].append(word)
            else:
                dictn[new]=[word]
        
        
        return list(dictn.values())  # Return grouped anagrams as lists


                
