nums=[1, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920,3265920]
for i in range(1,11):
    nums[i]=nums[i]+nums[i-1]
print(nums)