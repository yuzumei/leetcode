import random
import time
x=time.time()
num1=[]
num2=[]
for _ in range(100000):
    num1.append(random.randint(1,50))
    num2.append(random.randint(20,60))
num1.sort(reverse=True)
num2.sort(reverse=True)
y=time.time()
print(y-x)
ans=1
queue=[]
while num1:
    num=num1.pop(0)
    while num2 and num2[0]>=num:
        queue.append(num2.pop(0))
    if not queue:
        ans=0
        break
    ans*=len(queue)
    ans=ans%(10**9+7)
    queue.pop(0)
print(ans%(10**9+7))
print(time.time()-y)