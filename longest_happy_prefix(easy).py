class Solution:
    def longestPrefix(self, s: str) -> str:
        j=0
        i=1
        lps=[]
        lps.append(0)
        while(i<len(s)):
            if s[i]==s[j]:
                j=j+1
                lps.append(j)
                i=i+1
            else:
                if j==0:
                    lps.append(0)
                    i=i+1
                else:
                    j=lps[j-1]
                    
        print(lps)
        return s[:lps[-1]]