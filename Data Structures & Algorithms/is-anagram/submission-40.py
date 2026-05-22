class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
    
        countS, countJ = {}, {}

        for i in range (len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countJ[t[i]] = 1 + countJ.get(t[i],0)
        return countS == countJ

        