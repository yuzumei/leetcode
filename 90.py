class Solution:
    def subsetsWithDup(self, nums):
        ans=[]
        n=len(nums)
        def dfs(num,i):
            if i>=n:
                return
            temp=num+[nums[i]]
            ans.append(temp)
            dfs(temp,i+1)
            j=i+1
            while j<n and nums[j]==nums[i]:
                j+=1
            dfs(num,j)
        dfs([],0)
        return ans+[[]]
x=Solution()
print(x.subsetsWithDup([1]))