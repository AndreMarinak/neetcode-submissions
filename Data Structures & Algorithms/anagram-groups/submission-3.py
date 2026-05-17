class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={} #sorted; index
        ans=[]
        total=0
        for word in strs:
            correct="".join(sorted(word))
            if correct in groups:
                ans[groups[correct]].append(word)
            else:
                groups[correct]=total
                total+=1
                ans+=[[word]]

        return ans

        



