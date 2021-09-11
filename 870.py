A = [2,0,4,1,2]
B = [1,3,0,0,2]
tempa=sorted(A,reverse=True)
tempb=sorted(B,reverse=True)
tempdict={b:-1 for b in B}
ans=[0 for i in range(len(A))]
for item in tempb:
    if tempa[0]>item:
        for i in range(len(tempa)):
            if i==len(tempa)-1 or tempa[i+1]<=item:
                temp=B.index(item,tempdict[item]+1)
                tempdict[item]=temp
                ans[temp]=tempa[i]
                tempa.remove(tempa[i])
                break
    else:
        temp = B.index(item, tempdict[item])
        tempdict[item] = temp+1
        ans[temp] = tempa[-1]
        tempa.remove(tempa[-1])

print(ans)

