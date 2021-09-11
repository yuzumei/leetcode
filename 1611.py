def find():
    command = "URR"
    obstacles = [[4, 2]]
    x = 3
    y = 2
    location=[[0,0]]
    for item in command:
        x0=location[-1][0]
        y0=location[-1][1]
        if item=="U":
            location.append([x0,y0+1])
        else:
            location.append([x0+1,y0])
    interval=location[-1]
    count=min(x//interval[0],y//interval[1])
    if [x-count*interval[0],y-count*interval[1]] not in location:
        return False
    for item in obstacles:
        if item[0]>x or item[1]>y:
            continue
        count = min(item[0] // interval[0], item[1] // interval[1])
        if [item[0]-count*interval[0],item[1]-count*interval[1]] in location:
            return False
    return True

print(find())