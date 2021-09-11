class Solution:
    def find(self,strlist):
        import collections
        def matach(s1,s2):
            if len(s1)<len(s2):
                return matach(s2,s1)
            if len(s1)-len(s2)>=2:
                return False
            if len(s1)==len(s2):
                cnt=0
                for i in range(len(s1)):
                    if s1[i]!=s2[i]:
                        cnt+=1
                    if cnt>=2:
                        return False
                return True
            if len(s1)==len(s2)+1:
                left=0
                right=0
                while left<len(s1) and right<len(s2):
                    if s1[left]!=s2[right]:
                        left+=1
                    else:
                        left+=1
                        right+=1
                return True if right==len(s2) else False
        memo=collections.defaultdict(list)
        for i in range(len(strlist)):
            for j in range(i):
                if matach(strlist[i],strlist[j]):
                    memo[i].append(j)
        dp=[1]*len(strlist) #以第i项为末尾的最长值
        for i in range(len(strlist)):
            for j in memo[i]:
                dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
x=Solution()
test=['ace','ade','bcef','bceg','bcegh','da','dba','ae','aef','ace','ade','bcef','bceg','bcegh','da','dba','ae','aef','ace','ade','bcef','bceg','bcegh','da','dba','ae','aef','ace','ade','bcef','bceg','bcegh','da','dba','ae','aef''ace','ade','bcef','bceg','bcegh','da','dba','ae','aef','ace','ade','bcef','bceg','bcegh','da','dba','ae','aef','ace','ade','bcef','bceg','bcegh','da','dba','ae','aef']
print(x.find(test))