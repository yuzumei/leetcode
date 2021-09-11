class Solution:
    def countPairs(self, nums, low: int, high: int) -> int:
        n=len(bin(max(nums))[2:])
        trie=dict()
        ans=0
        for num in nums:
            flag=1
            temp=''
            temptrie=trie
            another=trie
            cnt=n
            while cnt!=0:
                s=1 if num>=2**(cnt-1) else 0
                num-=s*(2**(cnt-1))
                if not another:
                    flag=0
                else:
                    if 1-s in another:
                        temp += '1'
                        another=another[1-s]
                    else:
                        temp += '0'
                        another = another[s]
                if s not in temptrie:
                    temptrie[s]=dict()
                temptrie=temptrie[s]
                cnt-=1
            if flag==1:
                if low<=int(temp,2)<=high:
                    ans+=1
        return ans
x=Solution()
print(x.countPairs([9,8,4,2,1],5,14))