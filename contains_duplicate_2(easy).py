class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==0:
            return -1
        hmap={}
        hmap[nums[0]]=0
        for i in range(1,len(nums)):
            if nums[i] in hmap.keys():
                j=hmap[nums[i]]
                if abs(i-j)<=k:
                    return True
            hmap[nums[i]]=i
        return False