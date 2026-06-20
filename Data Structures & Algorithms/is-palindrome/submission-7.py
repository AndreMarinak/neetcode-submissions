class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().lower()

        
        p1=0
        p2=(len(s)-1)
        while p1<=p2:
            if s[p1].isalnum() != True:
                p1+=1
                continue
            if s[p2].isalnum() !=True:
                p2-=1
                continue
            elif s[p1] != s[p2]:
                return False
            else:
                p1+=1
                p2-=1
        return True 
