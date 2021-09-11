nums = [12,345,2,6,7896]
count=0
def even(num):
    if num//10>0:
        return 1+even(num//10)
    return 1
count=0
for i in nums:
    if even(i)%2==0:
        count+=1
print(count)