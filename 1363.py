class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        memo=[0]*10
        sums=0
        for num in digits:
            memo[num]+=1
            sums+=num
        temp=sums%3
        if temp!=0:
            if memo[temp]+memo[temp+3]+memo[temp+6]!=0:
                while memo[temp]==0:
                    temp+=3
                memo[temp]-=1
            else:
                if memo[3-temp]+memo[6-temp]+memo[9-temp]>=2:
                    cnt=2
                    i=3-temp
                    while cnt!=0:
                        tempcnt=min(cnt,memo[i])
                        memo[i]-=tempcnt
                        i+=3
                        cnt-=tempcnt
                else:
                    return ''
        ans=''
        for i in range(9,-1,-1):
            ans+=('%d'%i)*memo[i]
        return str(int(ans)) if ans else ''
x=Solution()
print(x.largestMultipleOfThree(digits = [5,8]))