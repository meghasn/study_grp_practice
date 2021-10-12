class Solution:
    def __init__(self):
        self.result=[]
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums,0,[],[0 for i in range(len(nums))])
        return self.result
    def backtracking(self,nums,index,path,visited):
        #base
        #logic
        for i in range(len(nums)):
            
            if visited[i]==0:
                visited[i]=1
                path.append(nums[i])
                print(path)
                print(visited)
                if len(path)==len(nums):
                    self.result.append(copy.copy(path))
                    
                self.backtracking(nums,i,path,visited)
                path.pop()
                visited[i]=0
        