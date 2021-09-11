row=[0,1,3,2]
newrow=row[:]
for i in range(0,len(row),2):
    if row[i]%2==0 and row[i+1]==row[i]+1:
        newrow.remove(row[i])
        newrow.remove(row[i+1])
    if row[i] % 2 == 1 and row[i + 1] == row[i] - 1:
        newrow.remove(row[i])
        newrow.remove(row[i+1])
def exchange(nums):
    if nums[0]%2==0:
        if nums[1]==nums[0]+1:
            return False
        else:
            temp=nums.index(nums[0]+1)
            nums[1],nums[temp]=nums[temp],nums[1]
            return True
    else:
        if nums[1]==nums[0]-1:
            return False
        else:
            temp=nums.index(nums[0]-1)
            nums[1],nums[temp]=nums[temp],nums[1]
            return True
index=0
n=len(newrow)
cnt=0
while len(newrow)!=0:
    if exchange(newrow):
        cnt+=1
    newrow=newrow[2:]
print(cnt)
