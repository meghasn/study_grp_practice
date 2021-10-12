#O(n) time complexity
#O(1) 26 characters max
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        print(s)
        hmap={}
        for i in range(len(s)):#O(n)
            hmap[s[i]]=i
        print(hmap)
        index=hmap[s[0]]
        x=0
        result=[]
        for i in range(len(s)):#O(n)
            index=max(index,hmap[s[i]])
            print()
            if i==index:
                result.append(i-x+1)
                x=i+1
        return result