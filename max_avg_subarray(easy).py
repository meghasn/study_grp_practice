class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        print(nums[:k])
        s=sum(nums[:k])
        avg=s/k
        print(avg)
        print(len(nums)-k)
        for i in range(len(nums)-k):
            print("a")
            print(nums[i])
            s=s+nums[i+k]-nums[i]
            a=s/k
            
            if a>avg:
                print(a)
                avg=a
        return avg
            
        
        