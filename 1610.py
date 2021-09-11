points = [[2,1],[2,2],[3,4],[1,1]]
angle = 90
location = [1,1]
import math
import bisect
temp=[]
maxnum=0
fixed=0
for item in points:
    if item[0]==location[0]:
        if item[1]>location[1]:
            bisect.insort(temp,90)
        elif item[1]==location[1]:
            fixed+=1
        else:
            bisect.insort(temp,270)
    else:
        rec=math.atan((item[1]-location[1])/(item[0]-location[0]))*180/math.pi
        if item[1]<location[1]:
            rec+=360
        bisect.insort(temp,rec)
print(temp)
for i in range(len(temp)):
    if temp[i]<=90:
        temp.append(temp[i]+360)
    refer=temp[i]+angle
    bisect.insort(temp, refer)
    maxnum=max(maxnum,temp.index(refer)-i)
    temp.remove(refer)
print(maxnum+fixed)