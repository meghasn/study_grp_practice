# // Time Complexity :O(logn), binary search
# // Space Complexity :O(n),hashmap
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :can probably optimize the code(too muchchecking using if-else)


# // Your code here along with comments explaining your approach



class TimeMap:

    def __init__(self):
        self.hmap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap.keys():
            self.hmap[key]=[]
        self.hmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap.keys():
            return ""
        li=self.hmap[key]
        low=0
        high=len(li)-1
        while(low<=high):
            mid=(low+high)//2
            if li[mid][1]==timestamp:
                return li[mid][0]
            elif li[mid][1]<timestamp:
                if mid+1 == len(li):
                    return li[mid][0]
                low=mid+1
            else:
                if mid-1 == -1:
                    return ""
                elif li[mid-1][1]<timestamp:
                    return li[mid-1][0]
                else:
                    high=mid-1
        
       
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)